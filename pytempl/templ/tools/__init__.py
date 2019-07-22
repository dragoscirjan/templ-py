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

    autopep8 = providers.Singleton(Autopep8, config.app)
    black = providers.Singleton(Black, config.app)


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
