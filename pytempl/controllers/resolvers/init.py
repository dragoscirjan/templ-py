from functools import reduce

import logging

from .base import BaseResolver
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.git.tools import BaseTool
from pytempl.os import file_exists, str2bool


class Init(BaseResolver):

    _new = False

    _inquire_list = {}
    _answers_list = {}

    _hooks_config = None
    """Git Hooks Config"""

    def __init__(
            self,
            hooks_config: HooksConfig,
            logger: logging.Logger,
            args: dict = None,
            inquire_list: list = None,
            git_tools_list: list = None
        ):
        super().__init__(logger=logger, args=args)
        self._new = args.get('new', False)
        self._hooks_config = hooks_config
        self._inquire_list = inquire_list if inquire_list else []
        self._git_tools_list = [item() for item in git_tools_list] if git_tools_list else []

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
        self.inquire().compile().write()

    def inquire(self):
        if not self._new:
            return self
        for inquire in list(map(lambda item: item(), self._inquire_list)):
            self._answers_list[inquire.key] = inquire.ask().answers
        return self

    def compile(self):
        """
        Compile user choices into the application config
        :return:
        """
        if not self._new:
            return self
        config = {
            HooksConfig.HOOK_PRE_COMMIT: self._compile_precommit()
        }
        self._hooks_config.from_dict(config)
        return self

    def write(self):
        """
        Write Config
        :return:
        """
        self._write_hook()
        self.
        if self._new:
            self._hooks_config.write()
        return self

    def _compile_precommit(self):
        answers = self._answers_list[HooksConfig.HOOK_PRE_COMMIT]
        
        tools = []
        for category in BaseTool.CATEGORIES:
            if category == BaseTool.CATEGORY_EDITORCONFIG and answers.get(category, None):
                tools += [BaseTool.CATEGORY_EDITORCONFIG]
            else:
                tools += answers.get(category, []) if isinstance(answers.get(category, None), list) else [answers.get(category, None)]
        tools = list(filter(lambda item: item, tools))
        
        code_tools = list(filter(lambda item: item.TOKEN in tools, self._git_tools_list))

        commands = {}
        for tool in code_tools:
            for ext in tool.config.get('ext'):
                if not ext in commands:
                    commands[ext] = []
                if tool.config.get('hook', None):
                    commands[ext].append(tool.config.get('hook'))

        return {
            HooksConfig.KEY_PRE_COMMANDS: list(reduce(
                lambda a, b: a + b,
                filter(
                    lambda item: item,
                    map(
                        lambda item: item.config.get('prepend-pre-commit', None),
                        code_tools
                    )
                ),
                []
            )),
            HooksConfig.KEY_COMMANDS: commands,
            HooksConfig.KEY_POST_COMMANDS:  list(reduce(
                lambda a, b: a + b,
                filter(
                    lambda item: item,
                    map(
                        lambda item: item.config.get('append-pre-commit', None),
                        code_tools
                    )
                ),
                []
            )),
        }