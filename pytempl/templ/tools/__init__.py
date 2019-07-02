from .base import Base
from .base_req import BaseReq

from .bandit import Bandit
from .black import Black
from .editorconfig import Editorconfig
from .flake8 import Flake8
from .isort import Isort
from .jsonlint import Jsonlint
from .mccabe import Mccabe
from .mypy import Mypy
from .pycodestyle import Pycodestyle
from .pydocstyle import Pydocstyle
from .pylint import Pylint
from .pytest import Pytest
from .radon import Radon
from .unittest import Unittest
from .yamllint import Yamllint


def __get_order(klass):
    return getattr(klass, 'ORDER', -1)


active_precommit_tools = [
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
    Pylint,
    Pytest,
    Radon,
    Unittest,
    Yamllint
]

active_precommit_tools.sort(key=__get_order)
