from .base import BaseTool


class Mypy(BaseTool):
    """
    :see: http://mypy-lang.org/
    """

    TOKEN = 'mypy'

    ORDER = BaseTool.ORDER_LINTER

    CATEGORY = BaseTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.mypy.ini': 'https://templ-project.github.io/python-configs/.mypy.ini'
            },
            'hook': 'mypy --config-file .mypy.ini',
            'name': 'MyPy (http://mypy-lang.org/)',
            'packages': ['mypy']
        })
