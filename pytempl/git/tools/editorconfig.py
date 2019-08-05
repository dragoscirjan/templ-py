from .base import BaseToolReq
from pytempl.os import str2bool


class Editorconfig(BaseToolReq):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = BaseToolReq.CATEGORY_EDITORCONFIG

    ORDER = BaseToolReq.ORDER_EDITORCONFIG

    CATEGORY = 'editorconfig'

    def _init_config(self):
        self.config.update({
            'files': {
                '.editorconfig': 'https://templ-project.github.io/python-configs/.editorconfig'
            },
            'name': 'Editorconfig (https://editorconfig.org/)'
        })
