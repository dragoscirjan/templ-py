from pytempl.templ.tools import Base


class Bandit(Base):
    """
    :see: https://github.com/PyCQA/bandit
    """

    TOKEN = 'bandit'

    ORDER = 70

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.bandit': 'https://raw.githubusercontent.com/PyCQA/pylint/master/.bandit'
            },
            'hook': 'bandit -ini .bandit',
            'packages': ['bandit']
        })
