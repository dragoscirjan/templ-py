from pytempl.code.base import BaseCodeTool


class Mccabe(BaseCodeTool):
    """
    :see: http://pypi.python.org/pypi/mccabe
    """

    TOKEN = 'mccabe'

    ORDER = BaseCodeTool.ORDER_ANALYZER

    CATEGORY = BaseCodeTool.CATEGORY_ANALYZER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'python -m mccabe --min 5',
            'name': 'Mccabe (http://pypi.python.org/pypi/mccabe)',
            'packages': ['mccabe']
        })
