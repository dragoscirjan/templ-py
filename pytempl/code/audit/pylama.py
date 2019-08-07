from pytempl.code.base import BaseCodeTool


class Pylama(BaseCodeTool):
    """
    :see: https://github.com/klen/pylama
    """

    TOKEN = 'pylama'

    ORDER = BaseCodeTool.ORDER_AUDIT

    CATEGORY = BaseCodeTool.CATEGORY_AUDIT

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                'pylintrc': 'https://templ-project.github.io/python-configs/pylama.ini'
            },
            'hook': 'pylama',
            'name': 'Pylama (https://github.com/klen/pylama)',
            'packages': ['pylama']
        })
