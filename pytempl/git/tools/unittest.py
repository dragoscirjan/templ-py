from .base import BaseToolReq


class Unittest(BaseToolReq):
    """
    :see: https://docs.Unittest.org/en/latest/
    """

    TOKEN = 'unittest'

    ORDER = BaseToolReq.ORDER_UNITTEST

    CATEGORY = BaseToolReq.CATEGORY_UNITTEST

    def _init_config(self):
        self.config.update({
            'name': 'Unittest (https://docs.python.org/3.5/library/unittest.html)',
            'packages': [],
            'append-pre-commit': 'python -m unittest discover -s tests -p "*_test.py"'
        })
