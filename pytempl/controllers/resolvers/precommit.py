from .base import BaseResolver


class PreCommit(BaseResolver):

    def run(self):
        self.determine_files().compile_commands().process()

    def determine_files(self):
        """
        Determine files to process
        :return:
        """
        return self

    def compile_commands(self):
        """
        Compile commands to run for pre-commit
        :return:
        """
        return self

    def process(self):
        """
        Process commands
        :return:
        """
        return self