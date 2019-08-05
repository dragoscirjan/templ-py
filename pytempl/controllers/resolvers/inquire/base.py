from PyInquirer import prompt


class BaseInquire:

    _answers = {}
    _key = ''
    _questions = []

    def ask(self):
        self._answers[self._key] = prompt(self._questions)
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
