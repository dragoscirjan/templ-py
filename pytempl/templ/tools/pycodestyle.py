from pytempl.templ.tools import Base


class Pycodestyle(Base):
    """
    :see: https://github.com/PyCQA/pycodestyle
    :see: http://pycodestyle.pycqa.org
    """

    TOKEN = 'pycodestyle'

    ORDER = 40

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.pydocstylerc': 'https://github.com/dragoscirjan/templ-py/raw/master/.pydocstylerc'
            },
            'hook': 'pycodestyle --config .pydocstylerc',
            'name': 'PyCodeStyle (http://pycodestyle.pycqa.org)',
            'packages': ['pycodestyle']
        })
