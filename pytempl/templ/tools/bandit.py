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
                '.bandit': 'https://github.com/dragoscirjan/templ-py/raw/master/.bandit'
            },
            'hook': 'bandit -ini .bandit',
            'name': 'Bandit (https://github.com/PyCQA/bandit)',
            'packages': ['bandit']
        })
