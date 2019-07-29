from .base import Base


class JSONLint(Base):

    def run(self):
        self.determine_files().lint()

    def determine_files(self):
        """
        Determine JSON file to lint
        :return:
        """
        return self

    def lint(self):
        """
        Perform linting action
        :return:
        """
        return self