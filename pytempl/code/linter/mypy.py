from pytempl.code.base import BaseCodeTool


class Mypy(BaseCodeTool):
    """
    :see: http://mypy-lang.org/
    """

    TOKEN = 'mypy'

    ORDER = BaseCodeTool.ORDER_LINTER

    CATEGORY = BaseCodeTool.CATEGORY_LINTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.mypy.ini': 'https://templ-project.github.io/python-configs/mypy.ini'
            },
            'hook': 'mypy --config-file .mypy.ini',
            'name': 'MyPy (http://mypy-lang.org/)',
            'packages': ['mypy']
        })
