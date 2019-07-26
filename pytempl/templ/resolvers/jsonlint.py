import sys

import simplejson

from pytempl.templ import RED, YELLOW, pcprint, wcolour
from .base import Base


class Jsonlint(Base):

    @staticmethod
    def arguments() -> list:
        return [
            (['--file', '-f'],
             {'default': [],
              'dest': 'files',
              'help': 'Files to lint',
              'nargs': '+',
              'type': str})
        ]

    def run(self) -> None:
        """
        Command Resolver for precommit Command
        :return: None
        """
        if 0 == len(self.app.pargs.files):
            return
        for file in self.app.pargs.files:
            with open(file) as json_file:
                try:
                    simplejson.load(json_file)
                except simplejson.JSONDecodeError as ejd:
                    if 1 < len(self.app.pargs.files):
                        pcprint(file, colour=YELLOW)
                    pcprint("JSON object issue: {}".format(wcolour(ejd.msg, colour=YELLOW, ecolour=RED)), colour=RED)
                    sys.exit(1)
                except Exception as e:
                    if 1 < len(self.app.pargs.files):
                        pcprint(file, colour=YELLOW)
                    pcprint("JSON object issue: {}".format(wcolour(e, colour=YELLOW, ecolour=RED)), colour=RED)
                    sys.exit(1)
