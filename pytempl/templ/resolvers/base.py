from cement import App


class Base:

    app = None

    def __init__(self, app: App) -> None:
        self.app = app

    @staticmethod
    def arguments() -> list:
        """
        Return the list of arguments for a certain command
        :return: list
        """
        return []

    def run(self) -> None:
        """
        Command resolve
        :return:
        """
        pass
