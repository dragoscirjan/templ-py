from .base import Base

class Setup(Base):

    def run(self):
        self.inquire().compile().write()

    def inquire(self):
        """
        Ask user for setup details
        :return:
        """
        return self

    def compile(self):
        """
        Compile user choices into the application config
        :return:
        """
        return self

    def write(self):
        """
        Write Config
        :return:
        """
        return self