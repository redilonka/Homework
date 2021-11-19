import os
import re
import json
from abc import ABC, abstractmethod
from datetime import datetime
from collections import Counter, namedtuple
from subprocess import CompletedProcess, check_output


class ParserInterface(ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'parse') and
                callable(subclass.parse) and
                hasattr(subclass, 'analyze') and
                callable(subclass.analyze) and
                hasattr(subclass, 'save') and
                callable(subclass.save) or
                NotImplemented)

    @abstractmethod
    def parse(self):
        raise NotImplementedError

    @abstractmethod
    def analyze(self):
        raise NotImplementedError

    def print(self):
        print(self._output)

    @abstractmethod
    def save(self):
        raise NotImplementedError


class PSUXParser(ParserInterface):
    """
    Parser for ps aux command.

    Colect and structure following stats:
    - users
    - user processes
    - RAM Usage
    - CPU utilization
    - Most RAM usage processe
    - Most CPU utilize process
    """
    USER = 0
    RAM = 3
    RSS = 5
    PID = 1
    CPU = 2
    COMMAND = 10

    SYSTEM_USERS = (
        "daemon",
        "nobody",
    )

    def __init__(self, completed_process: CompletedProcess) -> None:
        self._result = "Empty"

        try:
            self.mem_total = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / 1024 / 1024
        except ValueError:
            out = check_output(['sysctl', 'hw.memsize'], universal_newlines=True)
            hit = re.match(r'^hw.memsize: ([0-9]+)$', out)
            self.mem_total = int(hit.group(1)) / 1024 / 1024

        self._users = None
        self._user_proccesses = None
        self._process_count = None
        self._ram_usage = None
        self._cpu_utilization = None
        self._most_mem_usage_process = None
        self._most_cpu_util_process = None
        self._output = ""

        self._completed_process = completed_process

        self.resorce = namedtuple("Resource", ["name", "stat_target"])

        self.resources_no_analyze = (
            self.resorce(self.RSS, "_most_mem_usage_process"),
            self.resorce(self.CPU, "_most_cpu_util_process"),
        )

    def parse(self):
        """
        Parse the command output.

        Parsing result: list[list[str]]
        """
        self._result = [
            re.sub(" +", "^_^", raw, 10).split("^_^") for raw in
            self._completed_process.stdout.read().decode("utf-8").split("\n")][1:-1]

    @classmethod
    def _is_system_user(cls, username):
        return username in cls.SYSTEM_USERS or re.match(r"^_", username)

    def _collect_users(self):
        """
        Collect users for a list of process.

        Filter for real users by skipping pattern `_username`.
        """
        self._users = {
            process[0] for process in
            self._result if not self._is_system_user(process[self.USER])
        }

    def _collect_user_procecces(self):
        self._user_proccesses = Counter(
            [process[self.USER] for process in
            self._result if not self._is_system_user(process[self.USER])])

    def _collect_process_count(self):
        self._process_count = len(self._result)

    def _collect_ram_usage(self):
        self._ram_usage = round(self.mem_total * round(sum([
            float(process[self.RAM]) for process in self._result
        ]), 1) / 100, 1)

    def _collect_cpu_utilization(self):
        self._cpu_utilization = round(sum(
            float(process[self.CPU]) for process in self._result
        ), 1)

    def _collect_resource_usage_process(self, resource, stat_target):
        if self._result:
            _resource_usage = float(self._result[0][resource])
            setattr(self, stat_target, self._result[0][self.COMMAND])
        else:
            _resource_usage = 0

        for process in self._result:
            if float(process[resource]) > _resource_usage:
                _resource_usage = float(process[resource])
                setattr(self, stat_target, process[self.COMMAND])

    def analyze(self):
        self._collect_users()
        self._collect_user_procecces()
        self._collect_process_count()
        self._collect_ram_usage()
        self._collect_cpu_utilization()

        for resource in self.resources_no_analyze:
            self._collect_resource_usage_process(resource.name, resource.stat_target)


        self._compile_output()

    def _compile_output(self):
        """
        Compile the text output.

        It seems like builtin python templating doesn't support
        for statements. So simple string concatenation will be used.
        """
        self._output += "Отчёт о состоянии системы:\n"
        self._output += f"Пользователи системы: {', '.join(self._users)}\n"
        self._output += f"Процесcов запущено: {self._process_count}\n\n"

        self._output += "Пользовательских процессов:\n"
        for user, process_count in self._user_proccesses.items():
            self._output += f"{user}: {process_count}\n"

        self._output += "\n"

        self._output += f"Всего памяти используется: {self._ram_usage} mb\n"
        self._output += f"Всего CPU используется: {self._cpu_utilization}%\n"

        self._output += f"Больше всего памяти использует: {self._most_mem_usage_process[:20]}\n"
        self._output += f"Больше всего CPU использует: {self._most_cpu_util_process.split('/')[-1][:20]}\n"

    def save(self):
        with open(f"homework11/{datetime.now().strftime('%m-%d-%Y-%H:%M:%S')}-scan.txt", "w") as f:
            f.write(self._output)


class AccessLogsParser(ParserInterface):
    METHOD = 2
    IP_ADDRESS = 0
    URL = 3
    REQUEST_TIME = -1

    TOP_LONG_REQUEST_COUNT = 3
    MOST_COMMON_IPS_COUNT = 3

    # There are some redundant groups like refferer and time
    # It will add some time to procceed large log files but can be used in future
    REQUEST_PATTERN = r'^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>.+)\] "(?P<details>(GET|POST|PUT|DELETE|HEAD|OPTIONS) .*)" (?P<status>.+) (?P<length>.+) "(?P<refferer>.*)" ".*" (?P<request_time>.+)'
    PATTERN = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} .+"

    def __init__(self, completed_process: CompletedProcess) -> None:
        self._completed_process = completed_process

        self._total_request_count = 0
        self._method_stats = None
        self._ip_stats = None
        self._long_requests = None
        self._output = ""
        self._output_json = {}
        self._broken_log = 0
        self._broken_log_list = []

    def parse(self):
        self._result = []
        for raw in self._completed_process.stdout.read().decode("utf-8").split("\n"):

            if not raw: continue

            if re.search(self.PATTERN, raw):
                self._total_request_count += 1

            if match := re.search(self.REQUEST_PATTERN, raw):
                # POST /administrator/index.php HTTP/1.1 -> ['POST', '/administrator/index.php', 'HTTP/1.1']
                details = match.groupdict()["details"].split(" ")

                self._result.append([
                    match.groupdict()["ip"],
                    match.groupdict()["time"],  # Don't use for now
                    details[0],
                    details[1],
                    int(match.groupdict()["status"]),
                    match.groupdict()["refferer"],  # Redundant item
                    int(match.groupdict()["request_time"]),
                ])
            else:
                self._broken_log += 1
                self._broken_log_list.append(raw)

    def _collect_method_stats(self):
        self._method_stats = Counter([request[self.METHOD] for request in self._result])

    def _collect_ip_stats(self):
        self._ip_stats = Counter([request[self.IP_ADDRESS] for request in self._result])

    def _collect_long_requests(self):
        self._result.sort(key=lambda request: request[self.REQUEST_TIME], reverse=True)
        self._long_requests = self._result[:self.TOP_LONG_REQUEST_COUNT]

    def _collect_broken_get_requests(self):
        for raw in self._broken_log_list:
            if re.search('"GET ', raw):
                self._method_stats["GET"] += 1

    def analyze(self):
        self._collect_method_stats()
        self._collect_ip_stats()
        self._collect_long_requests()
        self._collect_broken_get_requests()

        self._compile_output()

    def _compile_output(self):
        """
        Compile the text output.

        It seems like builtin python templating doesn't support
        for statements. So simple string concatenation will be used.
        """
        self._output += f"Общее количество выполненных запросов: {self._total_request_count}\n\n"
        self._output_json["total_request_count"] = self._total_request_count

        self._output += f"Количество запросов по типу: "
        self._output += ", ".join([f"{method}: {count}" for method, count in self._method_stats.items()])
        self._output += "\n\n"
        self._output_json["method_stats"] = self._method_stats

        self._output += f"Топ 3 IP адресов, с которых были сделаны запросы: \n"
        self._output += "".join([
            f"IP: {ip}: {count} запросов\n"
            for ip, count in self._ip_stats.most_common(self.MOST_COMMON_IPS_COUNT)])
        self._output += "\n"
        self._output_json["ip_stats"] = self._ip_stats.most_common(self.MOST_COMMON_IPS_COUNT)

        self._output += f"Топ 3 самых долгих запросов: \n"
        self._output += "".join([
            f"Method: {request[self.METHOD]} URL: {request[self.URL]} IP: {request[self.IP_ADDRESS]} Time: {request[self.REQUEST_TIME]/1000000} сек\n"
            for request in self._long_requests])
        self._output_json["long_requests"] = self._long_requests
        self._output += "\n"
        self._output += f"Сломанных записей: {self._broken_log}\n"

    def save(self):
        filename = f"homework11/{datetime.now().strftime('%m-%d-%Y-%H:%M:%S')}-access-log-analysis.json"

        with open(filename, "w") as f:
            json.dump(self._output_json, f, indent=4)
            print(f"Сохранен json файл {filename}\n")

