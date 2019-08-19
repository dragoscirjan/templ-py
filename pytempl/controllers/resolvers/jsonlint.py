import sys

import simplejson

from pytempl.os import file_exists
from .base import BaseResolver


class JSONLint(BaseResolver):

    EXIT_INVALID_FILE = 1
    EXIT_INVALID_JSON = 2

    _files = []
    """Files to lint"""

    @staticmethod
    def arguments() -> list:
        """
        Obtain list of arguments for
        :return: list
        """
        return [
            (['--file', '-f'],
             {'default': [],
              'dest': 'files',
              'help': 'Files to lint',
              'nargs': '+',
              'type': str})
        ]

    def run(self):
        self.determine_files().lint()

    def determine_files(self):
        """
        Determine JSON file to lint
        :return: self
        """
        self._files = self._args.get('files', [])
        self._logger.debug('JSONLINT > Discovered files [{}]'.format(' '.join(self._files)))
        return self

    def lint(self):
        """
        Perform linting action
        :return: self
        """
        if not self._files:
            self._logger.warning('JSONLINT > No files to test.')
            return self
        for file in self._files:
            if not file_exists(file):
                self._logger.warning('JSONLINT > File issue: (blue){} does not exist.'.format(file))
                sys.exit(self.EXIT_INVALID_FILE)
            with open(file) as json_file:
                try:
                    simplejson.load(json_file)
                except simplejson.JSONDecodeError as ejd:
                    self._logger.error("JSON object issue: {} ".format(str(ejd)))
                    sys.exit(self.EXIT_INVALID_JSON)
                except Exception as e: #pylint: disable=broad-except
                    self._logger.error("JSON object issue: {} ".format(str(e)))
                    sys.exit(self.EXIT_INVALID_JSON)
        return self
