from pytempl.templ.tools import BaseReq


class Isort(BaseReq):
    """
    :see: https://github.com/timothycrosley/isort
    """

    ORDER = 10

    TOKEN = 'isort'

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'hook': 'isort',
            'name': 'Isort (https://github.com/timothycrosley/isort)',
            'packages': ['isort']
        })
