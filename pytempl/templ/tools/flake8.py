from pytempl.templ.tools import Base


class Flake8(Base):
    """
    :see: http://flake8.pycqa.org
    :see: https://github.com/PyCQA/flake8
    """

    TOKEN = 'flake8'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.flake8': 'https://raw.githubusercontent.com/PyCQA/pylint/master/.flake8'
            },
            'hook': 'flake8 --show-source',
            'packages': ['flake8']
        })
