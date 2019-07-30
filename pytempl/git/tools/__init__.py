from dependency_injector import containers, providers

from .base import Base #isort:skip
from .base_req import BaseReq #isort:skip
from .autopep8 import Autopep8 #isort:skip
from .bandit import Bandit #isort:skip
from .black import Black #isort:skip
from .editorconfig import Editorconfig #isort:skip
from .flake8 import Flake8 #isort:skip
from .isort import Isort #isort:skip
from .jsonlint import Jsonlint #isort:skip
from .mccabe import Mccabe #isort:skip
from .mypy import Mypy #isort:skip
from .pycodestyle import Pycodestyle #isort:skip
from .pydocstyle import Pydocstyle #isort:skip
from .pylama import Pylama #isort:skip
from .pylint import Pylint #isort:skip
from .pytest import Pytest #isort:skip
from .radon import Radon #isort:skip
from .unittest import Unittest #isort:skip
from .unittestcov import Unittestcov #isort:skip
from .yamllint import Yamllint #isort:skip




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
