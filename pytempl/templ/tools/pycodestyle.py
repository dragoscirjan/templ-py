from pytempl.templ.tools import Base


class Pyflakes(Base):
    """
    :see: https://github.com/PyCQA/pycodestyle
    :see: http://pycodestyle.pycqa.org
    """

    TOKEN = 'pycodestyle'

    ORDER = 40

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.pycodestyle': 'https://raw.githubusercontent.com/PyCQA/pylint/master/.pycodestyle'
            },
            'hook': 'pycodestyle --config .pycodestyle',
            'packages': ['pycodestyle']
        })
