import sys
import simplejson

from .base import BaseResolver
from pytempl.os import file_exists


class JSONLint(BaseResolver):

    EXIT_INVALID_FILE = 1
    EXIT_INVALID_JSON = 2

    _files = []
    """Files to lint"""

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

    def run(self):
        self.determine_files().lint()

    def determine_files(self):
        """
        Determine JSON file to lint
        :return:
        """
        self._files = self._args.get('files', [])
        self._logger.debug('JSONLINT > Discovered files [{}]'.format(' '.join(self._files)))
        return self

    def lint(self):
        """
        Perform linting action
        :return:
        """
        if not self._files:
            self._logger.warn('JSONLINT > No files to test.')
            return
        for file in self._files:
            if not file_exists(file):
                self._logger.warn('JSONLINT > File issue: (blue){} does not exist.'.format(file))
                sys.exit(self.EXIT_INVALID_FILE)
            with open(file) as json_file:
                try:
                    simplejson.load(json_file)
                except simplejson.JSONDecodeError as ejd:
                    self._logger.error("JSON object issue: {} ".format(str(ejd)))
                    sys.exit(self.EXIT_INVALID_JSON)
                except Exception as e: #pylint: disable=W0703
                    self._logger.error("JSON object issue: {} ".format(str(e)))
                    sys.exit(self.EXIT_INVALID_JSON)
        return self