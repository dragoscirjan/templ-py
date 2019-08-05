from .base import BaseTool


class Pylama(BaseTool):
    """
    :see: https://github.com/klen/pylama
    """

    TOKEN = 'pylama'

    ORDER = BaseTool.ORDER_AUDIT

    CATEGORY = BaseTool.CATEGORY_AUDIT

    def _init_config(self):
        self.config.update({
            'files': {
                'pylintrc': 'https://templ-project.github.io/python-configs/pylama.ini'
            },
            'hook': 'pylama',
            'name': 'Pylama (https://github.com/klen/pylama)',
            'packages': ['pylama']
        })
