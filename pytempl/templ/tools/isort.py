from pytempl.templ.tools import BaseReq


class Isort(BaseReq):
    """
    :see: https://github.com/timothycrosley/isort
    """

    ORDER = BaseReq.ORDER_FORMATTER

    TOKEN = 'isort'

    CATEGORY = BaseReq.CATEGORY_FORMATTER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'files': {
                'isort.cfg': 'https://github.com/dragoscirjan/templ-py/raw/master/isort.cfg'
            },
            'hook': 'isort',
            'name': 'Isort (https://github.com/timothycrosley/isort)',
            'packages': ['isort']
        })
