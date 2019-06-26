from pytempl.tools import Base


class Editorconfig(Base):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = 'editorconfig'

    ORDER = 0

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.editorconfig': 'https://github.com/dragoscirjan/templ-py/raw/master/.editorconfig'
            }
        })
