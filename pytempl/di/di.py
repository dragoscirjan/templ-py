from dependency_injector import containers, providers
import logging

from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.git.tools import *
from pytempl.controllers.resolvers import JSONLint, PreCommit, Init

class DI(containers.DeclarativeContainer):

    config = providers.Configuration('config')

    logger = providers.Singleton(logging.Logger, name='pytempl')

    git = providers.Singleton(Git, logger=logger)
    git_hooks_config = providers.Singleton(HooksConfig, logger=logger)

    init = providers.Factory(Init, logger=logger)
    jsonlint = providers.Factory(JSONLint, logger=logger)
    precommit = providers.Factory(
        PreCommit,
        logger=logger,
        git=git,
        hooks_config=git_hooks_config,
    )

    autopep8 = providers.Singleton(Autopep8, app=config.app)
    mypy = providers.Singleton(Mypy, app=config.app)
    black = providers.Singleton(Black, app=config.app)
    isort = providers.Singleton(Isort, app=config.app)
    radon = providers.Singleton(Radon, app=config.app)
    bandit = providers.Singleton(Bandit, app=config.app)
    flake8 = providers.Singleton(Flake8, app=config.app)
    mccabe = providers.Singleton(Mccabe, app=config.app)
    pylama = providers.Singleton(Pylama, app=config.app)
    pylint = providers.Singleton(Pylint, app=config.app)
    pytest = providers.Singleton(Pytest, app=config.app)
    jsonlint = providers.Singleton(Jsonlint, app=config.app)
    unittest = providers.Singleton(Unittest, app=config.app)
    yamllint = providers.Singleton(Yamllint, app=config.app)
    pydocstyle = providers.Singleton(Pydocstyle, app=config.app)
    pycodestyle = providers.Singleton(Pycodestyle, app=config.app)
    unittestcov = providers.Singleton(Unittestcov, app=config.app)
    editorconfig = providers.Singleton(Editorconfig, app=config.app)