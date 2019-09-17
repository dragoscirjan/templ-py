import abc

from pytempl.core.loggable import Loggable
from pytempl.os import file_backup, file_exists, file_write, run_shell_command


class BaseHook(Loggable):

    _hook_type = None
    """"""

    def __init__(self, logger: Loggable.Logger):
        super().__init__(logger=logger)
        self._hook_type = None

    @property
    def hook_type(self):
        return self._hook_type

    def write_hook(self):
        hook_file = '.git/hooks/{}'.format(self._hook_type)
        command = self._hook_type.replace('-', '')

        if file_exists(path=hook_file):
            self._logger.debug('Backing up `{}` old file'.format(hook_file))
            file_backup(hook_file)

        content = """#! /bin/bash

pytempl {command}

# exit 1
""".format(command=command)

        file_write(content=content, path=hook_file)
        run_shell_command('chmod 766 {}'.format(hook_file))

        self._logger.info('{} created'.format(hook_file))

    @abc.abstractmethod
    def compile_config(self, answers):
        pass
