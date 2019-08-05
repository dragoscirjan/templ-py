import logging

from .base import BaseResolver
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.os import file_exists, str2bool


class Init(BaseResolver):

    _inquire_list = {}
    _answers_list = {}

    _hooks_config = None
    """Git Hooks Config"""

    def __init__(self, hooks_config: HooksConfig, logger: logging.Logger, args: dict = None, inquire_list: list = None):
        super().__init__(logger=logger, args=args)
        self._hooks_config = hooks_config
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
        self.inquire().compile()

    def inquire(self):
        for inquire in list(map(lambda item: item(), self._inquire_list)):
            self._answers_list[inquire.key] = inquire.ask().answers
        return self

    def compile(self):
        """
        Compile user choices into the application config
        :return:
        """
        config = {
            HooksConfig.HOOK_PRE_COMMIT: self._compile_precommit()
        }
        self._hooks_config.from_dict(config)
        return self

    def _compile_precommit(self):
        return {
            HooksConfig.KEY_PRE_COMMANDS: [],
            HooksConfig.KEY_COMMANDS: {},
            HooksConfig.KEY_POST_COMMANDS: []
        }


    def write(self):
        """
        Write Config
        :return:
        """
        print(self._hooks_config.to_dict())
        # self._hooks_config.write()
        return self