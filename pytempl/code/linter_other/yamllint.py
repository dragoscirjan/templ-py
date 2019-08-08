from pytempl.code.base import BaseToolReq


class Yamllint(BaseToolReq):
    """
    :see: https://github.com/tangwz/yamllint/
    :see: https://pypi.org/project/yamllint/
    """

    TOKEN = 'yamllint'

    ORDER = BaseToolReq.ORDER_LINTER_OTHER

    CATEGORY = BaseToolReq.CATEGORY_LINTER_OTHER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'ext': ['*.yaml', '*.yml'],
            'files': {
                '.yamllint': 'https://templ-project.github.io/python-configs/yamllint'
            },
            'hook': 'yamllint -c .yamllint',
            'name': 'Yamllint (https://github.com/tangwz/yamllint)',
            'packages': ['yamllint']
        })
