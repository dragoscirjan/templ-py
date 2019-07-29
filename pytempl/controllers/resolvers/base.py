

class Base:

    args: dict = {}
    """Resolver Arguments"""

    def __init__(self, args: dict = None):
        """

        :param args: dict
        """
        self.args = args if args else {}

    def run(self):
        pass