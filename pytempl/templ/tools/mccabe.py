from pytempl.templ.tools import Base


class Mccabe(Base):
    """
    :see: http://pypi.python.org/pypi/mccabe
    """

    TOKEN = 'mccabe'

    ORDER = 80

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'python -m mccabe --min 5',
            'name': 'Mccabe (http://pypi.python.org/pypi/mccabe)',
            'packages': ['mccabe']
        })
