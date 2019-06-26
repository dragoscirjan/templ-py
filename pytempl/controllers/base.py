from cement import Controller, ex
from cement.utils.version import get_version_banner
from functools import reduce

from pytempl.core.version import get_version
from pytempl.tools import Base as BaseTool, active_tools

VERSION_BANNER = """
Pre-Commit Python Lint/Formatter Configurator %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Pre-Commit Python Lint/Formatter Configurator'

        # text displayed at the bottom of --help output
        epilog = 'Usage: pytempl command1 --foo bar'

        # controller level arguments. ex: 'pytempl --version'
        arguments = [
            ### add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='Use to configure the lint/format tools.',

        # sub-command level arguments. ex: 'pytempl command1 --foo bar'
        arguments= [
            ### add a sample foo option under subcommand namespace
            (['--interactive'],
             {'default': False,
              'dest': 'interactive',
              'help': 'Run configure with interactive wizzard.',
              'nargs': '?',
              'type': bool}),
            (['--reconfig'],
             {'default': False,
              'dest': 'reconfig',
              'help': 'Reconfigure all installed tools.',
              'nargs': '?',
              'type': bool}),
            (['--silent'],
             {'default': False,
              'dest': 'silent',
              'help': 'Silent run. Logging is disabled.',
              'nargs': '?',
              'type': bool}),
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
    )
    def precommit(self):
        """Use to configure the lint/format tools."""

        for klass in active_tools:
            klass(app=self.app).run()

        # data = {
        #     'foo': 'bar',
        # }
        #
        # ### do something with arguments
        # if self.app.pargs.foo is not None:
        #     data['foo'] = self.app.pargs.foo
        #
        # self.app.render(data, 'command1.jinja2')
