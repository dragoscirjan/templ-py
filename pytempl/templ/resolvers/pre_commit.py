from functools import reduce

from pytempl.templ.resolvers import Base as BaseResolver
from pytempl.templ.hooks import Collection, PreCommit as PreCommitHook, Init as InitHook
from pytempl.templ.tools import Base as BaseTool, active_precommit_tools
from pytempl.templ.utils import str2bool


class PreCommit(BaseResolver):
    @staticmethod
    def arguments() -> list:
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
        tools = []
        packages = []
        for klass in active_precommit_tools:
            tool = klass(app=self.app)
            tool.validate()
            tools.append(tool)
            packages += tool._config.get('packages', [])

        for tool in tools:
            tool.run()

        hook = self._create_hook(tools=tools, klass=PreCommitHook)
        collection = self._load_collection()
        collection.add_hook(hook_type=Collection.TYPE_PRECOMMIT, hook=hook, force=True)

        init = collection.get_hook(Collection.TYPE_INIT)
        if init is None:
            init = InitHook()
        init.store_command('precommit')
        collection.add_hook(hook_type=Collection.TYPE_INIT, hook=init, force=True)
        collection.to_file()

        self._check_packages(packages=packages)





