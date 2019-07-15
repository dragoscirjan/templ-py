from pytempl.templ.tools import BaseReq


class Pylint(BaseReq):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = 'pylint'

    ORDER = BaseReq.ORDER_LINTER

    CATEGORY = BaseReq.CATEGORY_LINTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                'pylintrc': 'https://raw.githubusercontent.com/PyCQA/pylint/master/pylintrc'
            },
            'hook': 'pylint',
            'name': 'Pylint (https://www.pylint.org/)',
            'packages': ['pylint']
        })
