from pytempl.core import Loggable
from pytempl.git.hooks import HooksConfig
from pytempl.os import str2bool
from pytempl.pip import Pip
from .base import BaseResolver


class Init(BaseResolver):
    _new = False

    _inquire_list = {}
    _answers_list = {}

    _pip = None

    _hooks_config = None
    """Git Hooks Config"""

    _hooks_list = []
    """List of Git Hooks"""

    def __init__(self, logger: Loggable.Logger, hooks_config: HooksConfig, pip: Pip, args: dict = None,
                 inquire_list: list = None, hooks_list: list = None):
        super().__init__(logger=logger, args=args)

        self._hooks_config = hooks_config

        self._pip = pip
        print(args)
        self._pip.set_requirements(args.get('requirements', None))
        self._pip.set_requirements_dev(args.get('requirements_dev', None))

        if inquire_list and isinstance(inquire_list, list):
            self._inquire_list = inquire_list

        if hooks_list and isinstance(hooks_list, list):
            self._hooks_list = list(map(lambda item: item(), hooks_list))

        self._new = args.get('new', False)

    @staticmethod
    def arguments() -> list:
        return [
            (['--new'],
             {'const': True,
              'default': False,
              'dest': 'new',
              'help': 'Initialize setup query and create new config.',
              'nargs': '?',
              'type': str2bool}),
            (['--requirements'],
             {'const': True,
              'default': False,
              'dest': 'requirements',
              'help': 'Requirements file. Default: requirements.txt',
              'nargs': '?',
              'default': 'requirements.txt',
              'type': str}),
            (['--requirements-dev'],
             {'const': True,
              'default': False,
              'dest': 'requirements_dev',
              'help': 'Requirements dev file. Default: requirements-dev.txt',
              'nargs': '?',
              'default': 'requirements-dev.txt',
              'type': str})
        ]

    def run(self):
        self.inquire().compile().write()

    def inquire(self):
        if not self._new:
            return self
        self._pip.read_dependencies()
        # for inquire in list(map(lambda item: item(), self._inquire_list)):
        #     self._answers_list[inquire.key] = inquire.ask().answers
        self._answers_list = {'pre-commit': {'editorconfig': 'editorconfig', 'audit': 'flake8', 'unittest': 'pytest',
                                             'linter_other': ['jsonlint', 'yamllint']}}
        return self

    def compile(self):
        """
        Compile user choices into the application config
        :return:
        """
        if not self._new:
            return self
        config = {}
        for hook in self._hooks_list:
            config[hook.hook_type] = hook.compile_config(self._answers_list.get(hook.hook_type, {}))
        self._hooks_config.from_dict(config)
        return self

    def write(self):
        """
        Write Config
        :return:
        """
        for hook in self._hooks_list:
            hook.write_hook()
        if self._new:
            self._hooks_config.write()
        self._pip.write_dependencies()
        return self
