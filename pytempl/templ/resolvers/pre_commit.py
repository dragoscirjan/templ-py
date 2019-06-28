from functools import reduce

from pytempl.templ.resolvers import Base
# from pytempl.hooks import Collection
from pytempl.tools import Base as BaseTool, active_tools
from pytempl.utils import str2bool


class PreCommit(Base):
    @staticmethod
    def arguments() -> list:
        return [
            ### add a sample foo option under subcommand namespace
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
             {'default': False,
              'dest': 'prepend_pre_commit',
              'help': 'Add custom pre-commit command at end of list.',
              'nargs': '?',
              'type': str})
        ] + reduce((lambda a, b: a + b), [BaseTool.arguments(klass) for klass in active_tools]),

    def run(self) -> None:
        super().run()
