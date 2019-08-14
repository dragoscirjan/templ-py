from pytempl.code.base import BaseCodeTool


class Radon(BaseCodeTool):
    """
    :see: https://radon.readthedocs.io/en/latest/
    """

    TOKEN = 'radon'

    ORDER = BaseCodeTool.ORDER_ANALYZER

    CATEGORY = BaseCodeTool.CATEGORY_ANALYZER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'radon cc --min B --max E',
            'name': 'Radon (https://radon.readthedocs.io/en/latest/)',
            'packages': ['radon']
        })
