import logging

from .base import BaseResolver
from pytempl.git import Git


class PreCommit(BaseResolver):

    _git = None
    """Git Handler"""

    _files = []

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

    def __init__(self, logger: logging.Logger, git: Git, args: dict = None):
        super().__init__(logger, args)
        self._git = git

    def run(self):
        self.determine_files().compile_commands().process()

    def determine_files(self):
        """
        Determine files to process
        :return:
        """
        self._files = self._args.get('files', [])
        if not self._files:
            self._files = self._git.diff_list_files()
        self._logger.debug('Precommit parsing following files: [{}]'.format(', '.join(self._files)))
        return self

    def compile_commands(self):
        """
        Compile commands to run for pre-commit
        :return:
        """
        return self

    def process(self):
        """
        Process commands
        :return:
        """
        return self