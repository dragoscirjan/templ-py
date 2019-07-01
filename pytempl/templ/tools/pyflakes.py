from pytempl.templ.tools import Base


class Pyflakes(Base):
    """
    :see: https://github.com/PyCQA/pyflakes
    TODO: Add message for flake8: If you want a more configurable tool, please used flake8
    """

    TOKEN = 'pyflakes'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'pyflakes',
            'name': 'Pyflakes (https://github.com/PyCQA/pyflakes)',
            'packages': ['pyflakes']
        })
