from .base import BaseTool


class Flake8(BaseTool):
    """
    :see: http://flake8.pycqa.org
    :see: https://github.com/PyCQA/flake8
    """

    TOKEN = 'flake8'

    ORDER = BaseTool.ORDER_AUDIT

    CATEGORY = BaseTool.CATEGORY_AUDIT

    def _init_config(self):
        self.config.update({
            'files': {
                '.flake8': 'https://templ-project.github.io/python-configs/.flake8'
            },
            'hook': 'flake8 --show-source',
            'name': 'Flake8 (http://flake8.pycqa.org)',
            'packages': ['flake8']
        })
