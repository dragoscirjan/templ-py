import sys
import simplejson

from .base import BaseResolver
from pytempl.os import file_exists, str2bool
from pytempl.controllers.resolvers.inquire import InquireHooks, InquirePreCommit


class Init(BaseResolver):

    EXIT_INVALID_FILE = 1
    EXIT_INVALID_JSON = 2

    _files = []
    """Files to lint"""

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
        for  klass in [
            InquireHooks,
            InquirePreCommit,
        ]:
            print(klass().ask().answers)