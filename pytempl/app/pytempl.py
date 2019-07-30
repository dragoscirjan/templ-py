from cement import App, init_defaults
from cement.core.exc import CaughtSignal

from pytempl.controllers.base import Base

# configuration defaults
CONFIG = init_defaults('pytempl')
CONFIG['pytempl']['foo'] = 'bar'


class PyTempl(App):
    """PyTempl primary application."""

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