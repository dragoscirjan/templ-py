# import logging
import loguru


class Loggable:

    _logger = None

    # Logger = logging.Logger
    Logger = loguru._Logger

    # def __init__(self, logger: logging.Logger):
    def __init__(self, logger: loguru._Logger):
        self._logger = logger

