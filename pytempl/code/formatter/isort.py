from pytempl.code.base import BaseToolReq


class Isort(BaseToolReq):
    """
    :see: https://github.com/timothycrosley/isort
    """

    ORDER = BaseToolReq.ORDER_FORMATTER

    TOKEN = 'isort'

    CATEGORY = BaseToolReq.CATEGORY_FORMATTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.isort.cfg': 'https://templ-project.github.io/python-configs/isort.cfg'
            },
            'hook': 'isort',
            'name': 'Isort (https://github.com/timothycrosley/isort)',
            'packages': ['isort']
        })
