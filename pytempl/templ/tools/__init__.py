from .base import Base
from .black import Black
from .editorconfig import Editorconfig
from .flake8 import Flake8
from .isort import Isort
from .pylint import Pylint


def __get_order(klass):
    return getattr(klass, 'ORDER', -1)


active_precommit_tools = [
    Editorconfig,
    Isort,
    Pylint
]

active_precommit_tools.sort(key=__get_order)
