from pytempl.templ.tools import Base


class Flake8(Base):
    """
    :see: https://github.com/PyCQA/flake8
    """

    TOKEN = 'flake8'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                'pylintrc': 'https://raw.githubusercontent.com/PyCQA/pylint/master/pylintrc'
            },
            'hook': 'flake8',
            'packages': ['flake8']
        })
