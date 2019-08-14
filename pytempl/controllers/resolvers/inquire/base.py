from PyInquirer import prompt

from pytempl.core import Loggable


class BaseInquire(Loggable):

    _answers = {}
    _key = ''
    _questions = []

    def ask(self):
        self._answers = prompt(self._questions)
        return self

    @property
    def answers(self) -> dict:
        return self._answers

    @property
    def key(self) -> str:
        return self._key

    @property
    def questions(self) -> list:
        return self._questions
