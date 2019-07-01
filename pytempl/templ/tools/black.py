from pytempl.templ.tools import Base


class Black(Base):
    """
    :see: https://github.com/python/black
    TODO: Min py version is 3.6
    """

    ORDER = 10

    TOKEN = 'black'

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.black.toml': 'https://github.com/dragoscirjan/templ-py/raw/master/.black.toml'
            },
            'hook': 'black --config .black.toml',
            'name': 'Black (https://github.com/python/black)',
            'packages': ['black']
        })
