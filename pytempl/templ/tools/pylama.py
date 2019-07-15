from pytempl.templ.tools import Base


class Pylama(Base):
    """
    :see: https://github.com/klen/pylama
    """

    TOKEN = 'pylama'

    ORDER = Base.ORDER_AUDIT

    CATEGORY = Base.CATEGORY_AUDIT

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                'pylintrc': 'https://raw.githubusercontent.com/PyCQA/pylint/master/pylama.ini'
            },
            'hook': 'pylama',
            'name': 'Pylama (https://github.com/klen/pylama)',
            'packages': ['pylama']
        })
