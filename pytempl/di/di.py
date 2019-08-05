from dependency_injector import containers, providers
import logging

from pytempl.controllers.resolvers import *
from pytempl.controllers.resolvers.inquire import *
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.git.tools import *

class DI(containers.DeclarativeContainer):

    config = providers.Configuration('config')

    logger = providers.Singleton(logging.Logger, name='pytempl')

    git = providers.Singleton(Git, logger=logger)
    git_hooks_config = providers.Singleton(HooksConfig, logger=logger)

    autopep8 = providers.Singleton(Autopep8, logger=logger)
    mypy = providers.Singleton(Mypy, logger=logger)
    black = providers.Singleton(Black, logger=logger)
    isort = providers.Singleton(Isort, logger=logger)
    radon = providers.Singleton(Radon, logger=logger)
    bandit = providers.Singleton(Bandit, logger=logger)
    flake8 = providers.Singleton(Flake8, logger=logger)
    mccabe = providers.Singleton(Mccabe, logger=logger)
    pylama = providers.Singleton(Pylama, logger=logger)
    pylint = providers.Singleton(Pylint, logger=logger)
    pytest = providers.Singleton(Pytest, logger=logger)
    jsonlint = providers.Singleton(Jsonlint, logger=logger)
    unittest = providers.Singleton(Unittest, logger=logger)
    yamllint = providers.Singleton(Yamllint, logger=logger)
    pydocstyle = providers.Singleton(Pydocstyle, logger=logger)
    pycodestyle = providers.Singleton(Pycodestyle, logger=logger)
    unittestcov = providers.Singleton(Unittestcov, logger=logger)
    editorconfig = providers.Singleton(Editorconfig, logger=logger)

    inquire_hooks = providers.Singleton(InquireHooks)
    inquire_precommit = providers.Singleton(
        InquirePreCommit,
        git_tools_list=[
            autopep8,
            mypy,
            black,
            isort,
            radon,
            bandit,
            flake8,
            mccabe,
            pylama,
            pylint,
            pytest,
            jsonlint,
            unittest,
            yamllint,
            pydocstyle,
            pycodestyle,
            unittestcov,
            editorconfig
        ]
    )

    init = providers.Factory(
        Init,
        logger=logger,
        inquire_list=[
            inquire_hooks,
            # inquire_precommit,
        ]
    )
    jsonlint = providers.Factory(JSONLint, logger=logger)
    precommit = providers.Factory(
        PreCommit,
        logger=logger,
        git=git,
        hooks_config=git_hooks_config
    )