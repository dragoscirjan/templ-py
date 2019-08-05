from .base import BaseTool


class Pyflakes(BaseTool):
    """
    :see: https://github.com/PyCQA/pyflakes
    """

    TOKEN = 'pyflakes'

    ORDER = BaseTool.ORDER_LINTER

    CATEGORY = BaseTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'pyflakes',
            'name': 'Pyflakes (https://github.com/PyCQA/pyflakes)',
            'packages': ['pyflakes']
        })
