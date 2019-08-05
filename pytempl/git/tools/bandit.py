from .base import BaseTool


class Bandit(BaseTool):
    """
    :see: https://github.com/PyCQA/bandit
    """

    TOKEN = 'bandit'

    ORDER = BaseTool.ORDER_LINTER

    CATEGORY = BaseTool.CATEGORY_LINTER

    def _init_config(self):
        self.config.update({
            'files': {
                '.bandit': 'https://templ-project.github.io/python-configs/.bandit'
            },
            'hook': 'bandit -ini .bandit',
            'name': 'Bandit (https://github.com/PyCQA/bandit)',
            'packages': ['bandit']
        })
