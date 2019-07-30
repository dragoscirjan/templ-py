from pytempl.templ.tools import Base


class Pydocstyle(Base):
    """
    :see: https://github.com/PyCQA/pydocstyle
    :see: http://www.pydocstyle.org
    """

    TOKEN = 'pydocstyle'

    ORDER = Base.ORDER_LINTER

    CATEGORY = Base.CATEGORY_LINTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.pydocstylerc': 'https://templ-project.github.io/python-configs/.pydocstylerc'
            },
            'hook': 'pydocstyle --config .pydocstylerc',
            'name': 'Pydocstyle (http://www.pydocstyle.org)',
            'packages': ['pydocstyle']
        })
