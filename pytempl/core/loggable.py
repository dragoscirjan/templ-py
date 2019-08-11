import logging


class Loggable:

    _logger = None

    Logger = logging.Logger

    def __init__(self, logger: logging.Logger):
        self._logger = logger

