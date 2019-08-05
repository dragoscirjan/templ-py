from .base import BaseToolReq


class Pylint(BaseToolReq):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = 'pylint'

    ORDER = BaseToolReq.ORDER_LINTER

    CATEGORY = BaseToolReq.CATEGORY_LINTER

    def _init_config(self):
        self.config.update({
            'files': {
                '.pylintrc': 'https://templ-project.github.io/python-configs/.pylintrc'
            },
            'hook': 'pylint --rcfile=.pylintrc',
            'name': 'Pylint (https://www.pylint.org/)',
            'packages': ['pylint']
        })
