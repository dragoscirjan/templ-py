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
                '.pylintrc': 'https://templ-project.github.io/python-configs/.pylintrc'
            },
            'hook': 'pylint --rcfile=.pylintrc',
            'name': 'Pylint (https://www.pylint.org/)',
            'packages': ['pylint']
        })
