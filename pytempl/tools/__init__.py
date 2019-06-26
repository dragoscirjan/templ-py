from .base import Base
from .black import Black
from .editorconfig import Editorconfig
from .isort import Isort
from .pylint import Pylint


def __get_order(klass):
    return getattr(klass, 'ORDER', -1)


active_tools = [
    Editorconfig,
    Isort,
    Pylint
]

active_tools.sort(key=__get_order)
