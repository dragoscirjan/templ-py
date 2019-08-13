from cement import App, init_defaults
from cement.core.exc import CaughtSignal
from pprint import pprint
# import colorlog
# import logging
import sys

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
        # colorlog_formatter = colorlog.ColoredFormatter(">> %(log_color)s%(name)s %(reset)s>> %(log_color)s%(message)s",
        #                                                 datefmt=None,
        #                                                 reset=True,
        #                                                 log_colors={
        #                                                     'DEBUG': 'cyan',
        #                                                     'INFO': 'green',
        #                                                     'WARNING': 'yellow',
        #                                                     'ERROR': 'red',
        #                                                     'CRITICAL': 'red,bg_white',
        #                                                 },
        #                                                 secondary_log_colors={},
        #                                                 style='%')
        # colorlog_handler = colorlog.StreamHandler()
        # colorlog_handler.setFormatter(colorlog_formatter)
        # self.di.logger().addHandler(colorlog_handler)
        # self.di.logger().setLevel(logging.INFO)
        # config = {
        #     "handlers": [
        #         {"sink": sys.stderr, 'colorize': True, 'format': "{level} | {message}", 'filter': "pytempl", 'level': "DEBUG"}
        #     ]
        # }
        # self.di.logger().configure(**config)
        self.di.logger().remove()
        self.di.logger().add(sys.stdout, format=">> <lvl>{message}</lvl>", level="INFO")
        pprint(self.di.logger()._handlers)
        if self.debug:
            # self.di.logger().setLevel(logging.DEBUG)
            self.di.logger().add(sys.stdout, format=">> DBG <lvl>{message}</lvl>", level="DEBUG")
            pprint(self.di.logger()._handlers)

