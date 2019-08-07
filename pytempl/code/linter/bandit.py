from pytempl.code.base import BaseCodeTool


class Bandit(BaseCodeTool):
    """
    :see: https://github.com/PyCQA/bandit
    """

    TOKEN = 'bandit'

    ORDER = BaseCodeTool.ORDER_LINTER

    CATEGORY = BaseCodeTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.bandit': 'https://templ-project.github.io/python-configs/.bandit'
            },
            'hook': 'bandit -ini .bandit',
            'name': 'Bandit (https://github.com/PyCQA/bandit)',
            'packages': ['bandit']
        })
