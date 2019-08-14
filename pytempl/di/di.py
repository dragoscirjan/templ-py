from dependency_injector import containers, providers
# import logging
import loguru

from pytempl.controllers.resolvers import *
from pytempl.controllers.resolvers.inquire import *
from pytempl.code import *
from pytempl.git import Git
from pytempl.git.hooks import *
from pytempl.pip import Pip

class DI(containers.DeclarativeContainer):

    config = providers.Configuration('config')

    # logger = providers.Singleton(logging.Logger, name='pytempl')
    logger = providers.Singleton(loguru._Logger, None, 0, False, False, False, False, None, {})

    pip = providers.Singleton(Pip, logger=logger)

    code_tool_autopep8 = providers.Singleton(Autopep8, logger=logger, pip=pip)
    code_tool_mypy = providers.Singleton(Mypy, logger=logger, pip=pip)
    code_tool_black = providers.Singleton(Black, logger=logger, pip=pip)
    code_tool_isort = providers.Singleton(Isort, logger=logger, pip=pip)
    code_tool_radon = providers.Singleton(Radon, logger=logger, pip=pip)
    code_tool_bandit = providers.Singleton(Bandit, logger=logger, pip=pip)
    code_tool_flake8 = providers.Singleton(Flake8, logger=logger, pip=pip)
    code_tool_mccabe = providers.Singleton(Mccabe, logger=logger, pip=pip)
    code_tool_pylama = providers.Singleton(Pylama, logger=logger, pip=pip)
    code_tool_pylint = providers.Singleton(Pylint, logger=logger, pip=pip)
    code_tool_pytest = providers.Singleton(Pytest, logger=logger, pip=pip)
    code_tool_jsonlint = providers.Singleton(Jsonlint, logger=logger, pip=pip)
    code_tool_unittest = providers.Singleton(Unittest, logger=logger, pip=pip)
    code_tool_yamllint = providers.Singleton(Yamllint, logger=logger, pip=pip)
    code_tool_pydocstyle = providers.Singleton(Pydocstyle, logger=logger, pip=pip)
    code_tool_pycodestyle = providers.Singleton(Pycodestyle, logger=logger, pip=pip)
    code_tool_unittestcov = providers.Singleton(Unittestcov, logger=logger, pip=pip)
    code_tool_editorconfig = providers.Singleton(Editorconfig, logger=logger, pip=pip)

    code_tools_list = [
        code_tool_autopep8,
        code_tool_bandit,
        code_tool_black,
        code_tool_editorconfig,
        code_tool_flake8,
        code_tool_isort,
        code_tool_jsonlint,
        code_tool_mccabe,
        code_tool_mypy,
        code_tool_pycodestyle,
        code_tool_pydocstyle,
        code_tool_pylama,
        code_tool_pylint,
        code_tool_pytest,
        code_tool_radon,
        code_tool_unittest,
        code_tool_unittestcov,
        code_tool_yamllint,
    ]

    git = providers.Singleton(Git, logger=logger)
    git_hooks_config = providers.Singleton(HooksConfig, logger=logger)
    git_hooks_precommit = providers.Singleton(
        PreCommitHook,
        logger=logger,
        code_tools_list=code_tools_list
    )

    git_hooks_list = [
        git_hooks_precommit
    ]

    inquire_hooks = providers.Singleton(InquireHooks, logger=logger)

    inquire_precommit = providers.Singleton(
        InquirePreCommit,
        logger=logger,
        git_tools_list=code_tools_list
    )

    inquire_list = [
        # inquire_hooks,
        inquire_precommit,
    ]

    init = providers.Singleton(
        Init,
        logger=logger,
        inquire_list=inquire_list,
        hooks_config=git_hooks_config,
        hooks_list=git_hooks_list,
        pip=pip
    )
    jsonlint = providers.Factory(JSONLint, logger=logger)
    precommit = providers.Factory(
        PreCommit,
        logger=logger,
        git=git,
        hooks_config=git_hooks_config
    )
