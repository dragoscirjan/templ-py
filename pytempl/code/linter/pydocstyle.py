from pytempl.code.base import BaseCodeTool


class Pydocstyle(BaseCodeTool):
    """
    :see: https://github.com/PyCQA/pydocstyle
    :see: http://www.pydocstyle.org
    """

    TOKEN = 'pydocstyle'

    ORDER = BaseCodeTool.ORDER_LINTER

    CATEGORY = BaseCodeTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.pydocstylerc': 'https://templ-project.github.io/python-configs/.pydocstylerc'
            },
            'hook': 'pydocstyle --config .pydocstylerc',
            'name': 'Pydocstyle (http://www.pydocstyle.org)',
            'packages': ['pydocstyle']
        })
