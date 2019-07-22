from cement import Controller, ex
from cement.utils.version import get_version_banner

from pytempl.core.version import get_version
from pytempl.templ.resolvers import Jsonlint, Resolvers, PreCommitConfig

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
            # add a version banner
            (['-v', '--version'],
             {'action': 'version',
              'version': VERSION_BANNER}),
        ]

    resolvers = None

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.resolvers = Resolvers(config={'app': self.app})

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='Use to configure the lint/format tools.',
        # sub-command level arguments. ex: 'pytempl precommit-config'
        arguments=PreCommitConfig.arguments()
    )
    def precommit_config(self):
        """Use to configure the lint/format tools."""
        self.resolvers.pre_commit_config().run()
        # data = {
        #     'foo': 'bar',
        # }
        # self.app.render(data, 'command1.jinja2')

    @ex(
        help='Use to run configured lint/format tools from pre-commit hook.'
        # sub-command level arguments. ex: 'pytempl precommit'
    )
    def precommit(self):
        self.resolvers.pre_commit().run()

    @ex(
        help='Use to lint JSON files.',
        # sub-command level arguments. ex: 'pytempl jsonlint -f /path/to/file.json'
        arguments=Jsonlint.arguments()
    )
    def jsonlint(self):
        """Use to lint JSON files."""
        self.resolvers.jsonlint()(app=self.app).run()
