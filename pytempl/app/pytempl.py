from cement import App, init_defaults
from cement.core.exc import CaughtSignal
import logging

from pytempl.controllers.base import Base
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
        if self.debug:
            self.di.logger().setLevel(logging.DEBUG)
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

