from functools import reduce
import sys

from pytempl.templ.resolvers import Base as BaseResolver
from pytempl.templ.hooks import Collection as HookCollection, PreCommit as PreCommitHook
from pytempl.templ.tools import active_precommit_tools
from pytempl.templ.utils import str2bool
from pytempl.templ import pcprint, GREEN


class PreCommitConfig(BaseResolver):
    @staticmethod
    def arguments() -> list:
        """
        Obtain List of Arguments for precommit-config Command
        :return: list
        """
        return [
            (['--interactive'],
             {'const': True,
              'default': False,
              'dest': 'interactive',
              'help': 'Run configure with interactive wizzard.',
              'nargs': '?',
              'type': str2bool}),
            (['--reconfig'],
             {'const': True,
              'default': False,
              'dest': 'reconfig',
              'help': 'Reconfigure all installed tools.',
              'nargs': '?',
              'type': str2bool}),
            (['--silent'],
             {'const': True,
              'default': False,
              'dest': 'silent',
              'help': 'Silent run. Logging is disabled.',
              'nargs': '?',
              'type': str2bool}),
            (['--append-pre-commit'],
             {'default': [],
              'dest': 'append_pre_commit',
              'help': 'Add custom pre-commit command at beggining of list.',
              'nargs': '+',
              'type': str}),
            (['--prepend-pre-commit'],
             {'default': [],
              'dest': 'prepend_pre_commit',
              'help': 'Add custom pre-commit command at end of list.',
              'nargs': '+',
              'type': str})
        ] + reduce((lambda a, b: a + b), [klass.arguments(klass) for klass in active_precommit_tools])

    def run(self) -> None:
        """
        Command Resolver for precommit-config Command
        :return: None
        """
        self._check_hook_configured_and_exit(hook_type=HookCollection.TYPE_PRECOMMIT)

        tools = self._init_tools()
        required_packages = self._required_packages(tools)

        for tool in tools:
            tool.run()

        if self._can_reconfig():
            self._reconfig(klass=PreCommitHook, tools=tools, command='precommit')

        # TODO: Should be presented only at config action is taken
        # self._check_required_packages(packages=required_packages)

    def _init_tools(self) -> list:
        """
        Initialize `pytempl.templ.tools`
        :return: list
        """
        tools = []
        for klass in active_precommit_tools:
            tool = klass(app=self.app)
            tool.validate()
            tools.append(tool)
        return tools

    def _required_packages(self, tools: list) -> list:
        """
        Obtain list of packages requiered
        :param tools:
        :return: list
        """
        required_packages = list(map(lambda tool: tool._config.get('packages', []), tools))
        return list(reduce(lambda a, b: a + b, required_packages, []))



