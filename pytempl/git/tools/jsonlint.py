from .base import BaseToolReq


class Jsonlint(BaseToolReq):
    """
    :see: https://github.com/tangwz/jsonlint/
    :see: https://pypi.org/project/jsonlint/
    """

    TOKEN = 'jsonlint'

    ORDER = BaseToolReq.ORDER_LINTER_OTHER

    CATEGORY = BaseToolReq.CATEGORY_LINTER_OTHER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'ext': ['*.json'],
            'hook': 'pytempl jsonlint -f',
            'name': 'Jsonlint (https://github.com/tangwz/jsonlint)',
            'packages': ['simplejson']
        })
