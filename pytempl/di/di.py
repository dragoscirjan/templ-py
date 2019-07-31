from dependency_injector import containers, providers
import colorlog
import logging

from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.controllers.resolvers import JSONLint, PreCommit

class DI(containers.DeclarativeContainer):

    config = providers.Configuration('config')

    logger = providers.Singleton(logging.Logger, name='pytempl')

    git = providers.Singleton(Git, logger=logger)
    git_hooks_config = providers.Singleton(HooksConfig, logger=logger)

    jsonlint = providers.Factory(JSONLint, logger=logger)
    precommit = providers.Factory(
        PreCommit,
        logger=logger,
        git=git,
        hooks_config=git_hooks_config,
    )



colorlog_formatter = colorlog.ColoredFormatter(">> %(log_color)s%(name)s %(reset)s>> %(log_color)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%')
colorlog_handler = colorlog.StreamHandler()
colorlog_handler.setFormatter(colorlog_formatter)
DI.logger().addHandler(colorlog_handler)
DI.logger().setLevel(logging.INFO)