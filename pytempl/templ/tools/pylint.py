from pytempl.templ.tools import Base


class Pylint(Base):
    """
    :see: https://www.pylint.org/
    """

    @staticmethod
    def arguments(klass):
        return super().arguments_skip(klass)

    TOKEN = 'pyflakes'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                'pylintrc': 'https://raw.githubusercontent.com/PyCQA/pylint/master/pylintrc'
            },
            'hook': 'pylint',
            'packages': ['pyflakes']
        })
