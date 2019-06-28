from cement import Controller, ex
from cement.utils.version import get_version_banner

from pytempl.core.version import get_version
from pytempl.templ.resolvers import PreCommit

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
        arguments= PreCommit.arguments()
    )
    def precommit(self):
        """Use to configure the lint/format tools."""

        PreCommit(app=self._app)


        # self.app.hooks = Collection()
        #
        # for klass in active_tools:
        #     klass(app=self.app).run()

        # data = {
        #     'foo': 'bar',
        # }
        #
        # ### do something with arguments
        # if self.app.pargs.foo is not None:
        #     data['foo'] = self.app.pargs.foo
        #
        # self.app.render(data, 'command1.jinja2')
