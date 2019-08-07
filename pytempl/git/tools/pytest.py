from .base import BaseTool


class Pytest(BaseTool):
    """
    :see: https://docs.pytest.org/en/latest/
    """

    TOKEN = 'pytest'

    ORDER = BaseTool.ORDER_UNITTEST

    CATEGORY = BaseTool.CATEGORY_UNITTEST

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'name': 'Pytest (https://docs.pytest.org/en/latest/)',
            'packages': ['coverage', 'pytest', 'pytest-cov', 'pytest-xdist'],
            'append-pre-commit': ['pytest --cov=myproj tests/']
        })
