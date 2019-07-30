from pytempl.templ.tools import BaseReq


class Jsonlint(BaseReq):
    """
    :see: https://github.com/tangwz/jsonlint/
    :see: https://pypi.org/project/jsonlint/
    """

    TOKEN = 'jsonlint'

    ORDER = BaseReq.ORDER_LINTER_OTHER

    CATEGORY = BaseReq.CATEGORY_LINTER_OTHER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'ext': ['*.json'] + getattr(app.pargs, 'with_{}_extensions'.format(self.TOKEN), []),
            'hook': 'pytempl jsonlint -f',
            'name': 'Jsonlint (https://github.com/tangwz/jsonlint)',
            'packages': ['simplejson']
        })
