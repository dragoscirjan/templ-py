from cement import App


class Base:

    _app = None

    def __init__(self, app: App) -> None:
        self._app = app

    @staticmethod
    def arguments() -> list:
        return []

    def run(self) -> None:
        pass
