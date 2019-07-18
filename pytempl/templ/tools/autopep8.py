from pytempl.templ.tools import Base


class Autopep8(Base):
    """
    :see: https://github.com/hhatto/autopep8
    """

    ORDER = Base.ORDER_FORMATTER

    TOKEN = 'autopep8'

    CATEGORY = Base.CATEGORY_FORMATTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.pep8': 'https://github.com/dragoscirjan/templ-py/raw/master/.pep8'
            },
            'hook': 'autopep8 --global-config .pep8',
            'name': 'Autopep8 (https://github.com/hhatto/autopep8)',
            'packages': ['autopep8']
        })
