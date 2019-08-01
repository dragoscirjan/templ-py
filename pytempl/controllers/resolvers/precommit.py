import logging

from .base import BaseResolver
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig


class PreCommit(BaseResolver):

    _git = None
    """Git Handler"""

    _hooks_config = None
    """Git Hooks Config"""

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
            print(pext, commands)
        # for ext in extensions:
        #     for command in hook[BaseHook.KEY_COMMANDS].get(ext, []):
        #         for file in files.get(ext, []):
        #             commands.append((command, file))

        for command in hook_config.get(HooksConfig.KEY_POST_COMMANDS, []):
            self._commands.append((command, False))

        print(self._commands)
        return self

    def process(self):
        """
        Process commands
        :return:
        """
        return self