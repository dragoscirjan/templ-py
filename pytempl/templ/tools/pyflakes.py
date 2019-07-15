from pytempl.templ.tools import Base


class Pyflakes(Base):
    """
    :see: https://github.com/PyCQA/pyflakes
    """

    TOKEN = 'pyflakes'

    ORDER = Base.ORDER_LINTER

    CATEGORY = Base.CATEGORY_LINTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'pyflakes',
            'name': 'Pyflakes (https://github.com/PyCQA/pyflakes)',
            'packages': ['pyflakes']
        })
