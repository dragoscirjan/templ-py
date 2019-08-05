from .base import BaseTool


class Radon(BaseTool):
    """
    :see: https://radon.readthedocs.io/en/latest/
    """

    TOKEN = 'radon'

    ORDER = BaseTool.ORDER_ANALYZER

    CATEGORY = BaseTool.CATEGORY_ANALYZER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'hook': 'radon cc --min B --max E',
            'name': 'Radon (https://radon.readthedocs.io/en/latest/)',
            'packages': ['radon']
        })
