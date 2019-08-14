from pytempl.code.base import BaseCodeTool


class Pyflakes(BaseCodeTool):
    """
    :see: https://github.com/PyCQA/pyflakes
    """

    TOKEN = 'pyflakes'

    ORDER = BaseCodeTool.ORDER_LINTER

    CATEGORY = BaseCodeTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'pyflakes',
            'name': 'Pyflakes (https://github.com/PyCQA/pyflakes)',
            'packages': ['pyflakes']
        })
