from .base import BaseTool


class Pycodestyle(BaseTool):
    """
    :see: https://github.com/PyCQA/pycodestyle
    :see: http://pycodestyle.pycqa.org
    """

    TOKEN = 'pycodestyle'

    ORDER = BaseTool.ORDER_LINTER

    CATEGORY = BaseTool.CATEGORY_LINTER

    def _init_config(self):
        self.config.update({
            'files': {
                '.pydocstylerc': 'https://templ-project.github.io/python-configs/.pydocstylerc'
            },
            'hook': 'pycodestyle --config .pydocstylerc',
            'name': 'PyCodeStyle (http://pycodestyle.pycqa.org)',
            'packages': ['pycodestyle']
        })
