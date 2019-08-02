from dependency_injector import containers, providers
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