from .base import BaseTool


class Unittestcov(BaseTool):
    """
    :see: https://docs.Unittest.org/en/latest/
    """

    TOKEN = 'unittestcov'

    ORDER = BaseTool.ORDER_UNITTEST

    CATEGORY = BaseTool.CATEGORY_UNITTEST

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'name': 'Unittest + Coverage (https://docs.python.org/3.5/library/unittest.html)',
            'packages': ['coverage'],
            'append-pre-commit': ['python -m unittest discover -s tests -p "*_test.py"']
        })
