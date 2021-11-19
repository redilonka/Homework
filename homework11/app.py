import os
import re
from datetime import datetime
from collections import Counter, namedtuple
from subprocess import Popen, PIPE, CompletedProcess, check_output


class PSUXParser:
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

    def __init__(self, output: CompletedProcess) -> None:
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

        self._completed_process = output

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

    def print(self):
        print(self._output)

    def save_report(self):
        with open(f"homework11/{datetime.now().strftime('%m-%d-%Y-%H:%M:%S')}-scan.txt", "w") as f:
            f.write(self._output)


class Analyzer:
    def __init__(self, cmd, parser) -> None:
        self._cmd = cmd
        self._parser = parser

    def run(self) -> None:
        self._completed_process = Popen(self._cmd, stdout=PIPE)
        self._parse()

    def _parse(self):
        parser =self._parser(self._completed_process)
        parser.parse()
        parser.analyze()
        parser.print()
        parser.save_report()


if __name__ == "__main__":
    analyzer = Analyzer(cmd=["ps", "aux"], parser=PSUXParser)
    result = analyzer.run()
