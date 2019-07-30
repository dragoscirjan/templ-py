from pytempl.templ.tools import Base


class Mypy(Base):
    """
    :see: http://mypy-lang.org/
    """

    TOKEN = 'mypy'

    ORDER = Base.ORDER_LINTER

    CATEGORY = Base.CATEGORY_LINTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.mypy.ini': 'https://templ-project.github.io/python-configs/.mypy.ini'
            },
            'hook': 'mypy --config-file .mypy.ini',
            'name': 'MyPy (http://mypy-lang.org/)',
            'packages': ['mypy']
        })
