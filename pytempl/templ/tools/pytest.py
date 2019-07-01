from pytempl.templ.tools import Base


class Pytest(Base):
    """
    :see: https://docs.pytest.org/en/latest/
    """

    @staticmethod
    def arguments(klass):
        return super().arguments_skip(klass)

    TOKEN = 'pytest'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'pytest',
            'name': 'Pytest (https://docs.pytest.org/en/latest/)',
            'packages': ['pytest']
        })
