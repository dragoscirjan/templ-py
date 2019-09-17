from cement import App, init_defaults

from pytempl.controllers.base import Base
# from cement.core.exc import CaughtSignal
from pytempl.core.loggable import Loggable
from pytempl.di import DI

# configuration defaults
CONFIG = init_defaults('pytempl')
CONFIG['pytempl']['foo'] = 'bar'


class PyTempl(App):
    """PyTempl primary application."""

    di = {}
    """Dependency Injection Container"""

    def run(self):
        self.di = DI()
        self._setup_logger()
        return super().run()

    class Meta:
        label = 'pytempl'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base
        ]

    def _setup_logger(self):
        Loggable.setup_logger(self.di.logger(), debug=self.debug)
