from pytempl.templ.tools import Base


class Pydocstyle(Base):
    """
    :see: https://github.com/PyCQA/pydocstyle
    :see: http://www.pydocstyle.org
    """

    TOKEN = 'pydocstyle'

    ORDER = 41

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.pydocstylerc': 'https://github.com/dragoscirjan/templ-py/raw/master/.pydocstylerc'
            },
            'hook': 'pydocstyle --config .pydocstylerc',
            'name': 'Pydocstyle (http://www.pydocstyle.org)',
            'packages': ['pydocstyle']
        })
