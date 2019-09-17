import simplejson

from pytempl.core.loggable import Loggable


class BaseResolver(Loggable):

    _logger = None
    """Logger"""

    _args = {}
    """Resolver Arguments"""

    def __init__(self, logger: Loggable.Logger, args: dict = None):
        """
        Constructor
        :param logger: Loggable.Logger
        :param args: dict
        """
        super().__init__(logger=logger)

        self._args = args if args else {}
        self._logger.debug('{} resolver initialised with args: {}'.format(
            self.__class__.__name__,
            simplejson.dumps(args)
        ))

    def run(self):
        pass
