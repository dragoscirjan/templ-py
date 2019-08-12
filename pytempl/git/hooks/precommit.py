from functools import reduce

from pytempl.code import BaseCodeTool, Editorconfig
from pytempl.core import Loggable
from .base import BaseHook
from .hooks_config import HooksConfig


class PreCommitHook(BaseHook):
    _code_tools_list = []

    hook_key = HooksConfig.HOOK_PRE_COMMIT

    def __init__(self, logger: Loggable.Logger, code_tools_list: list = None):
        super().__init__(logger)

        if code_tools_list and isinstance(code_tools_list, list):
            self._code_tools_list = list(map(lambda item: item(), code_tools_list))

        self._hook_type = HooksConfig.HOOK_PRE_COMMIT

    def compile_config(self, answers):
        # get tools tokens from answers
        tools = map(lambda category: answers.get(category, None), BaseCodeTool.CATEGORIES)
        tools = filter(lambda item: item, tools)
        tools = map(lambda item: item if isinstance(item, list) else [item], tools)
        tools = reduce(lambda a, b: a + b, tools, [])
        # filter used tools from list
        code_tools = list(filter(lambda item: item.TOKEN in tools, self._code_tools_list))

        for tool in code_tools:
            tool.run()

        code_tools = list(filter(lambda item: item.TOKEN != Editorconfig.TOKEN, code_tools))

        commands = {}
        for extensions, hook in list(
                map(lambda item: (item.config.get('ext', None), item.config.get('hook', None)), code_tools)):
            for ext in extensions:
                if ext not in commands:
                    commands[ext] = []
                if hook:
                    commands[ext].append(hook)
        return {
            HooksConfig.KEY_PRE_COMMANDS: list(reduce(lambda a, b: a + b, filter(lambda item: item, map(
                lambda item: item.config.get('prepend-pre-commit', None), code_tools)), [])),
            HooksConfig.KEY_COMMANDS: commands,
            HooksConfig.KEY_POST_COMMANDS: list(reduce(lambda a, b: a + b, filter(lambda item: item, map(
                lambda item: item.config.get('append-pre-commit', None), code_tools)), [])),
        }
