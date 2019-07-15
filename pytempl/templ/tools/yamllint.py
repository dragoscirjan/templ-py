from pytempl.templ.tools import BaseReq


class Yamllint(BaseReq):
    """
    :see: https://github.com/tangwz/yamllint/
    :see: https://pypi.org/project/yamllint/
    """

    TOKEN = 'yamllint'

    ORDER = BaseReq.ORDER_LINTER_OTHER

    CATEGORY = BaseReq.CATEGORY_LINTER_OTHER

    def __init__(self, app=None):
        super().__init__(app)
        self._config.update({
            'ext': ['*.yaml', '*.yml'] + getattr(app.pargs, 'with_{}_extensions'.format(self.TOKEN), []),
            'files': {
                '.yamllint': 'https://github.com/dragoscirjan/templ-py/raw/master/.yamllint'
            },
            'hook': 'yamllint -c .yamllint',
            'name': 'Yamllint (https://github.com/tangwz/yamllint)',
            'packages': ['yamllint']
        })
