from pytempl.templ.utils import str2bool
from .base import Base


class BaseReq(Base):

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
        ] + Base._arguments(klass=klass)
