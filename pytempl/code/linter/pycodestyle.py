from pytempl.code.base import BaseCodeTool


class Pycodestyle(BaseCodeTool):
    """
    :see: https://github.com/PyCQA/pycodestyle
    :see: http://pycodestyle.pycqa.org
    """

    TOKEN = 'pycodestyle'

    ORDER = BaseCodeTool.ORDER_LINTER

    CATEGORY = BaseCodeTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.pydocstylerc': 'https://templ-project.github.io/python-configs/.pydocstylerc'
            },
            'hook': 'pycodestyle --config .pydocstylerc',
            'name': 'PyCodeStyle (http://pycodestyle.pycqa.org)',
            'packages': ['pycodestyle']
        })
