import os
import sys
import argparse
from subprocess import Popen, PIPE

sys.path.append(os.getcwd())
from homework11.parsers import PSUXParser


ap = argparse.ArgumentParser()
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
    args = vars(ap.parse_args())

    psaux = Analyzer(cmd=["ps", "aux"], parser=PSUXParser)
    psaux.run(save=bool(args["save"]))
