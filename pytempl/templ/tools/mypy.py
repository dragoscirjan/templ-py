from pytempl.templ.tools import Base


class Mypy(Base):
    """
    :see: http://mypy-lang.org/
    """

    TOKEN = 'mypy'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.mypy.ini': 'https://raw.githubusercontent.com/PyCQA/pylint/master/.mypy.ini'
            },
            'hook': 'mypy --config-file .mypy.ini',
            'packages': ['mypy']
        })
