from pytempl.templ.tools import Base


class Pytest(Base):
    """
    :see: https://docs.pytest.org/en/latest/
    """

    TOKEN = 'pytest'

    ORDER = Base.ORDER_UNITTEST

    CATEGORY = Base.CATEGORY_UNITTEST

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'pytest',
            'name': 'Pytest (https://docs.pytest.org/en/latest/)',
            'packages': ['coverage', 'pytest', 'pytest-cov', 'pytest-xdist'],
            'append-pre-commit': 'pytest --cov=myproj tests/'
        })
