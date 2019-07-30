
from cement import Controller, ex
from cement.utils.version import get_version_banner

from pytempl.controllers.resolvers import JSONLint
from pytempl.core.version import get_version
from pytempl.di import DI

VERSION_BANNER = """
Tool aggregator for python code analisys %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Tool aggregator for python code analisys'

        # text displayed at the bottom of --help output
        # TODO: Must change content
        epilog = 'Usage: pytempl command1 --foo bar'

        # controller level arguments. ex: 'pytempl --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
        ]

    # def __init__(self, *args, **kw):
    #     super().__init__(*args, **kw)
    #     self.di = DI()

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help='Use to lint JSON files.',
        # sub-command level arguments. ex: 'pytempl jsonlint -f /path/to/file.json'
        arguments=JSONLint.arguments()
    )
    def jsonlint(self):
        """Use to lint JSON files."""
        JSONLint(logger=DI.logger(), args=vars(self.app.pargss)).run()
        # DI.jsonlint(args=vars(self.app.pargs)).run()

    # @ex(
    #     help='example sub command1',
    #     # sub-command level arguments. ex: 'pytempl command1 --foo bar'
    #     arguments=[
    #         ### add a sample foo option under subcommand namespace
    #         ( [ '-f', '--foo' ],
    #           { 'help' : 'notorious foo option',
    #             'action'  : 'store',
    #             'dest' : 'foo' } ),
    #     ],
    # )
    # def command1(self):
    #     """Example sub-command."""
    #     data = {
    #         'foo' : 'bar',
    #     }
    #     ### do something with arguments
    #     if self.app.pargs.foo is not None:
    #         data['foo'] = self.app.pargs.foo
    #     self.app.render(data, 'command1.jinja2')
