from dependency_injector import providers, containers

from .base import Base
from .mypy import Mypy
from .black import Black
from .isort import Isort
from .radon import Radon
from .bandit import Bandit
from .flake8 import Flake8
from .mccabe import Mccabe
from .pylama import Pylama
from .pylint import Pylint
from .pytest import Pytest
from .autopep8 import Autopep8
from .base_req import BaseReq
from .jsonlint import Jsonlint
from .unittest import Unittest
from .yamllint import Yamllint
from .pydocstyle import Pydocstyle
from .pycodestyle import Pycodestyle
from .unittestcov import Unittestcov
from .editorconfig import Editorconfig


class Tools(containers.DeclarativeContainer):
    """Tools Container."""

    config = providers.Configuration('config')

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


def __get_order(klass):
    return getattr(klass, 'ORDER', -1)


active_precommit_tools = [
    Autopep8,
    Bandit,
    Black,
    Editorconfig,
    Flake8,
    Isort,
    Jsonlint,
    Mccabe,
    Mypy,
    Pycodestyle,
    Pydocstyle,
    Pylama,
    Pylint,
    Pytest,
    Radon,
    Unittest,
    Unittestcov,
    Yamllint
]

active_precommit_tools.sort(key=__get_order)
