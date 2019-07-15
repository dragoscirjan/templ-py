import sys

from pytempl.templ import RED, pcprint
from pytempl.templ.tools import Base


class Black(Base):
    """
    :see: https://github.com/python/black
    """

    ORDER = 10

    TOKEN = 'black'

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.black.toml': 'https://github.com/dragoscirjan/templ-py/raw/master/.black.toml'
            },
            'hook': 'black --config .black.toml',
            'name': 'Black (https://github.com/python/black)',
            'packages': ['black']
        })

    def validate(self):
        if self._app.pargs.with_black is True and (sys.version_info[0] < 3 or sys.version_info[1] < 6):
            pcprint('Black requires python 3.6 or higher. Please used `Isort` for python 3.5.')
            sys.exit(10)

