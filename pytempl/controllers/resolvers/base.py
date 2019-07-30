import logging


class BaseResolver:

    _logger = None
    """Logger"""

    _args = {}
    """Resolver Arguments"""

    def __init__(self, logger: logging.Logger, args: dict = None):
        """

        :param logger: logging.Logger
        :param args: dict
        """
        self._logger = logger
        self._args = args if args else {}

    def run(self):
        pass