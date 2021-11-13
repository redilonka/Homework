import re
import sys,os
import argparse
from subprocess import Popen, PIPE

sys.path.append(os.getcwd())
from homework11.parsers import AccessLogsParser



ap = argparse.ArgumentParser()
ap.add_argument("-d", "--log_dir", required=False, help="Log files dir")
ap.add_argument("-f", "--access_file", required=False, help="Log file")
ap.add_argument('--save', action='store_true', default=False)


class Analyzer:
    def __init__(self, cmd, parser) -> None:
        self._cmd = cmd
        self._parser = parser

    def run(self) -> None:
        self._completed_process = Popen(self._cmd, stdout=PIPE)
        self._parse()

    def run(self, save: bool) -> None:
        self._completed_process = Popen(self._cmd, stdout=PIPE)
        self._parse(save)

    def _parse(self, save=False):
        parser =self._parser(self._completed_process)
        parser.parse()
        parser.analyze()
        parser.print()

        if save:
            parser.save()


if __name__ == "__main__":
    # Access log parser
    args = vars(ap.parse_args())

    _dir = str(args['log_dir'])
    if not _dir or _dir == "None":
        _dir = "."

    access_file = str(args['access_file']) or None

    cmd = ["cat"]

    if not access_file or access_file == "None":
        # For simplicity assume lall log files in a dir is apache2 log files
        log_files = [os.path.join(_dir, filename) for filename in
                     os.listdir(_dir) if re.match(r".+.log$", filename)]
        cmd.extend(log_files)
    else:
        cmd.append(access_file)

    print(f"Following command is about to start: {' '.join(cmd)}")

    access = Analyzer(cmd=cmd, parser=AccessLogsParser)
    access.run(save=bool(args["save"]))
