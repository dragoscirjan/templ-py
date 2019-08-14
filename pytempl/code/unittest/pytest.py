from pytempl.code.base import BaseCodeTool


class Pytest(BaseCodeTool):
    """
    :see: https://docs.pytest.org/en/latest/
    """

    TOKEN = 'pytest'

    ORDER = BaseCodeTool.ORDER_UNITTEST

    CATEGORY = BaseCodeTool.CATEGORY_UNITTEST

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'name': 'Pytest (https://docs.pytest.org/en/latest/)',
            'packages': ['coverage', 'pytest', 'pytest-cov', 'pytest-xdist'],
            'append-pre-commit': ['pytest --cov=myproj tests/']
        })
