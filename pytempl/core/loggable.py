# import logging
import sys

import loguru


class Loggable:

    _logger = None

    # Logger = logging.Logger
    Logger = loguru._Logger

    # def __init__(self, logger: logging.Logger):
    def __init__(self, logger: loguru._Logger):
        """
        Constructor
        :param logger: loguru._Logger
        """
        self._logger = logger

    @staticmethod
    def setup_logger(logger: loguru._Logger, debug: bool = False):
        """
        :param logger: loguru._Logger
        :param debug: bool (Default: False)
        :return: None
        """
        logger.remove()
        logger.add(sys.stdout, colorize=True, format=">> <lvl>{message}</lvl>", level="INFO")
        if debug:
            logger.add(sys.stdout, colorize=True, format=">> DBG <lvl>{message}</lvl>", level="DEBUG")
