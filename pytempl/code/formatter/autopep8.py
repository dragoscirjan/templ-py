from pytempl.code.base import BaseCodeTool


class Autopep8(BaseCodeTool):
    """
    :see: https://github.com/hhatto/autopep8
    """

    ORDER = BaseCodeTool.ORDER_FORMATTER

    TOKEN = 'autopep8'

    CATEGORY = BaseCodeTool.CATEGORY_FORMATTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.pep8': 'https://templ-project.github.io/python-configs/pep8'
            },
            'hook': 'autopep8 --global-config .pep8',
            'name': 'Autopep8 (https://github.com/hhatto/autopep8)',
            'packages': ['autopep8']
        })
