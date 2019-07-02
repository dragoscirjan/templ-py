from pytempl.templ.tools import BaseReq


class Unittest(BaseReq):
    """
    :see: https://docs.Unittest.org/en/latest/
    """

    TOKEN = 'unittest'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'unittest',
            'name': 'Unittest (https://docs.python.org/3.5/library/unittest.html)',
            'packages': ['coverage'],
            'append-pre-commit': 'python -m unittest discover -s tests -p "*_test.py"'
        })
