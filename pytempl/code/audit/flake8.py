from pytempl.code.base import BaseCodeTool


class Flake8(BaseCodeTool):
    """
    :see: http://flake8.pycqa.org
    :see: https://github.com/PyCQA/flake8
    """

    TOKEN = 'flake8'

    ORDER = BaseCodeTool.ORDER_AUDIT

    CATEGORY = BaseCodeTool.CATEGORY_AUDIT

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.flake8': 'https://templ-project.github.io/python-configs/flake8'
            },
            'hook': 'flake8 --show-source',
            'name': 'Flake8 (http://flake8.pycqa.org)',
            'packages': ['flake8']
        })
