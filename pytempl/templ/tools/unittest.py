from pytempl.templ.tools import BaseReq


class Unittest(BaseReq):
    """
    :see: https://docs.Unittest.org/en/latest/
    """

    TOKEN = 'unittest'

    ORDER = BaseReq.ORDER_UNITTEST

    CATEGORY = BaseReq.CATEGORY_UNITTEST

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'name': 'Unittest (https://docs.python.org/3.5/library/unittest.html)',
            'packages': [],
            'append-pre-commit': 'python -m unittest discover -s tests -p "*_test.py"'
        })
