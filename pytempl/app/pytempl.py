# import colorlog
# import logging
import sys

from cement import App, init_defaults

from pytempl.controllers.base import Base
from pytempl.di import DI

# from cement.core.exc import CaughtSignal


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
        self.di.logger().remove()
        self.di.logger().add(sys.stdout, colorize=True, format=">> <lvl>{message}</lvl>", level="INFO")
        if self.debug:
            self.di.logger().add(sys.stdout, colorize=True, format=">> DBG <lvl>{message}</lvl>", level="DEBUG")
        self.di.logger()
