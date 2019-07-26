from pytempl.templ.tools import BaseReq
from pytempl.templ.utils import str2bool


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

    @staticmethod
    def arguments(klass) -> list:
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
            (['--skip-{}'.format(klass.TOKEN)],
             {'const': True,
              'default': False,
              'dest': 'skip_{}'.format(klass.TOKEN),
              'help': 'skip installing `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': str2bool})
        ]
