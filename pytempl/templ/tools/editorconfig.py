from pytempl.templ.tools import BaseReq


class Editorconfig(BaseReq):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = BaseReq.CATEGORY_EDITORCONFIG

    ORDER = BaseReq.ORDER_EDITORCONFIG

    CATEGORY = 'editorconfig'

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                '.editorconfig': 'https://github.com/dragoscirjan/templ-py/raw/master/.editorconfig'
            },
            'name': 'Editorconfig (https://editorconfig.org/)'
        })
