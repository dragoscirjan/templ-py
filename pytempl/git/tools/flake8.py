from pytempl.templ.tools import Base


class Flake8(Base):
    """
    :see: http://flake8.pycqa.org
    :see: https://github.com/PyCQA/flake8
    """

    TOKEN = 'flake8'

    ORDER = Base.ORDER_AUDIT

    CATEGORY = Base.CATEGORY_AUDIT

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.flake8': 'https://templ-project.github.io/python-configs/.flake8'
            },
            'hook': 'flake8 --show-source',
            'name': 'Flake8 (http://flake8.pycqa.org)',
            'packages': ['flake8']
        })
