from .base import BaseTool


class Autopep8(BaseTool):
    """
    :see: https://github.com/hhatto/autopep8
    """

    ORDER = BaseTool.ORDER_FORMATTER

    TOKEN = 'autopep8'

    CATEGORY = BaseTool.CATEGORY_FORMATTER

    def _init_config(self):
        self.config.update({
            'files': {
                '.pep8': 'https://templ-project.github.io/python-configs/.pep8'
            },
            'hook': 'autopep8 --global-config .pep8',
            'name': 'Autopep8 (https://github.com/hhatto/autopep8)',
            'packages': ['autopep8']
        })
