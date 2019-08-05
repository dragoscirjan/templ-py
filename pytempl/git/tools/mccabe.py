from .base import BaseTool


class Mccabe(BaseTool):
    """
    :see: http://pypi.python.org/pypi/mccabe
    """

    TOKEN = 'mccabe'

    ORDER = BaseTool.ORDER_ANALYZER

    CATEGORY = BaseTool.CATEGORY_ANALYZER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'python -m mccabe --min 5',
            'name': 'Mccabe (http://pypi.python.org/pypi/mccabe)',
            'packages': ['mccabe']
        })
