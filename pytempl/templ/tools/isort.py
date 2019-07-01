from pytempl.templ.tools import Base


class Isort(Base):
    """
    :see: https://github.com/timothycrosley/isort
    """

    ORDER = 10

    TOKEN = 'isort'

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'isort',
            'packages': ['isort']
        })
