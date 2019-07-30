from pytempl.templ.tools import Base


class Unittestcov(Base):
    """
    :see: https://docs.Unittest.org/en/latest/
    """

    TOKEN = 'unittestcov'

    ORDER = Base.ORDER_UNITTEST

    CATEGORY = Base.CATEGORY_UNITTEST

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'name': 'Unittest + Coverage (https://docs.python.org/3.5/library/unittest.html)',
            'packages': ['coverage'],
            'append-pre-commit': 'python -m unittest discover -s tests -p "*_test.py"'
        })
