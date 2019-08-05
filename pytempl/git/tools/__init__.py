from .base import BaseTool, BaseToolReq #isort:skip
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
