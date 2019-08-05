import sys
import simplejson

import logging

from .base import BaseResolver
from pytempl.os import file_exists, str2bool


class Init(BaseResolver):

    EXIT_INVALID_FILE = 1
    EXIT_INVALID_JSON = 2

    _inquire_list = []

    def __init__(self, logger: logging.Logger, args: dict = None, inquire_list: list = None):
        super().__init__(logger=logger, args=args)
        self._inquire_list = inquire_list if inquire_list else []

    @staticmethod
    def arguments() -> list:
        return [
            (['--new'],
             {'const': True,
              'default': False,
              'dest': 'new',
              'help': 'Initialize setup query and create new config.',
              'nargs': '?',
              'type': str2bool})
        ]

    def run(self):
        for inquire in self._inquire_list:
            print(inquire.ask().answers)