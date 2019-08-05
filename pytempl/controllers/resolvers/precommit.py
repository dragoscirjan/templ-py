import logging
import re

from .base import BaseResolver
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.os.shell import run_shell_command


class PreCommit(BaseResolver):

    _git = None
    """Git Handler"""

    _hooks_config = None
    """Git Hooks Config"""

    _compiled_config = {}
    """Compiled config object"""

    _hook_type = None
    """Used Git Hook Type"""

    _files = []
    """Files to apply preconfig filters on"""

    _commands = []
    """Compiled commands to run"""

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

    def __init__(self, logger: logging.Logger, hooks_config: HooksConfig, git: Git, args: dict = None):
        super().__init__(logger, args)
        self._git = git
        self._hooks_config = hooks_config
        self._hook_type = HooksConfig.HOOK_PRE_COMMIT

    def run(self):
        self.determine_files().determine_config().compile_commands().process()

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

    def determine_config(self):
        self._hooks_config.read()
        return self

    def compile_commands(self):
        """
        Compile commands to run for pre-commit
        :return:
        """
        hook_config = self._hooks_config.to_dict().get(self._hook_type, {})

        for command in hook_config.get(HooksConfig.KEY_PRE_COMMANDS, []):
            self._commands.append((command, False))

        for pext, commands in hook_config.get(HooksConfig.KEY_COMMANDS, {}).items():
            for file in self._files:
                if re.compile(".{}$".format(pext.split('.')[1]), re.IGNORECASE).search(file):
                    for command in commands:
                        self._commands.append((command, file))

        for command in hook_config.get(HooksConfig.KEY_POST_COMMANDS, []):
            self._commands.append((command, False))
        return self

    def process(self):
        """
        Process commands
        :return:
        """
        for command, file in self._commands:
            self._logger.info('Running command `{} {}`'.format(command, file))
            run_shell_command(
                command='{} {}'.format(command, file) if file else command,
                print_output=True,
                raise_output=True
            )
            if (file):
                self._git.add(file=file)
        return self

    def inquire(self):
        """
        Ask user for setup details
        :return:
        """
        return self

    def compile(self):
        """
        Compile user choices into the application config
        :return:
        """
        return self

    def write(self):
        """
        Write Config
        :return:
        """
        config = self._hooks_config.to_dict()
        config[HooksConfig.HOOK_PRE_COMMIT] = self._compiled_config
        self._hooks_config.from_dict(config)
        self._hooks_config.write()
        return self