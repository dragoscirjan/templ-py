import logging

from pytempl.os import run_shell_command


class Git:
    
    def __init__(self, logger: logging.Logger):
        """
        Constructor
        :param logger: logging.Logger
        """
        self._logger = logger

    @staticmethod
    def _ll_diff(args: str = '', ) -> tuple:
        """
        Low Level Diff Method
        :param args: str
        :return: tuple(process, stdout, stderr)
        """
        return run_shell_command('git diff {}'.format(args))

    def add(self, file: str) -> bool:
        """
        Perform git add file
        :param file: str
        :return: bool
        """
        command = 'git add {}'.format(file)
        process, stdout, stderr = run_shell_command(command)
        if process.returncode > 0:
            self._logger.warning('`{}` failed with {}'.format(command, stderr))
            return False
        return True

    def diff(self, args: str = '', ) -> str:
        """
        Diff Method
        :param args: str
        :return: str|None
        """
        process, stdout, stderr = self._ll_diff(args=args)
        if process.returncode > 0:
            self._logger.warning(stderr)
            return None
        return stdout

    def diff_list_files(self) -> list:
        """
        Get list of files de
        :return: list
        """
        process, stdout, stderr = self._ll_diff(args='--cached --name-only')
        if process.returncode > 0:
            self._logger.warning('`git diff --cached --name-only` failed with'.format(stderr))
            return []
        return stdout.split("\n")
