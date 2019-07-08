import sys

from pytempl.templ import BLUE, GREEN, RED, pcprint, run_shell_command, wcolour
from pytempl.templ.hooks import Base as BaseHook
from pytempl.templ.hooks import Collection as HookCollection

from .base import Base


class PreCommit(Base):

    @staticmethod
    def arguments() -> list:
        return []

    def run(self) -> None:
        """
        Command Resolver for precommit Command
        :return: None
        """
        hook = self._get_precommit_hook()
        files = self._map_files_by_hook_extensions(files_list=self._get_changed_precommit_files())

        if hook[BaseHook.KEY_PRE_COMMANDS]:
            for command in hook[BaseHook.KEY_PRE_COMMANDS]:
                self._run_hook_command(command)

        for ext1 in hook[BaseHook.KEY_COMMANDS].keys():
            for ext2 in files:
                if ext1 == ext2:
                    for command in hook[BaseHook.KEY_COMMANDS][ext1]:
                        for file in files[ext2]:
                            if command and file:
                                c = command + ' ' + file
                                self._run_hook_command(c)
                                c = 'git add ' + file
                                self._run_hook_command(c)

        if hook[BaseHook.KEY_POST_COMMANDS]:
            for command in hook[BaseHook.KEY_POST_COMMANDS]:
                self._run_hook_command(command)

    def _get_precommit_hook(self) -> dict:
        """

        :return: dict
        """
        return self.hook_collection.get_hook(hook_type=HookCollection.TYPE_PRECOMMIT).to_dict()

    def _get_changed_precommit_files(self) -> list:
        """
        Get list of files de
        :return: list
        """
        stdout, stderr = run_shell_command(['git', 'diff', '--cached', '--name-only'])
        if stderr is not None:
            pass
        return stdout.decode().split("\n")

    def _run_hook_command(self, command: list) -> None:
        """

        :param command:
        :return:
        """
        pcprint('running ' + wcolour(command, colour=BLUE), colour=GREEN)
        stdout, stderr = run_shell_command(command)
        if stderr is not None:
            pcprint('error', colour=RED)
            print(stderr.decode())
            sys.exit()
