import os
import sys

from pytempl.templ import RED, BLUE, GREEN, YELLOW, pcprint, wcolour, run_shell_command
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

        if hook[BaseHook.KEY_PRE_COMMANDS] and len(hook[BaseHook.KEY_PRE_COMMANDS]):
            for command in hook[BaseHook.KEY_PRE_COMMANDS]:
                try:
                    self._run_hook_command(command.split(' '))
                except Exception as e:
                    pcprint('Error @ precommit:', colour=RED)
                    pcprint(e)
                    sys.exit(1)

        for ext1 in hook[BaseHook.KEY_COMMANDS].keys():
            for ext2 in files:
                if ext1 == ext2:
                    for command in hook[BaseHook.KEY_COMMANDS][ext1]:
                        for file in files[ext2]:
                            if command and file:
                                try:
                                    c = command + ' ' + file
                                    self._run_hook_command(c.split(' '))
                                    c = 'git add ' + file
                                    self._run_hook_command(c.split(' '))
                                except Exception as e:
                                    pcprint('Error @ precommit of: {}'.format(file, colour=YELLOW), colour=RED)
                                    pcprint(e)
                                    sys.exit(1)

        if hook[BaseHook.KEY_POST_COMMANDS] and len(hook[BaseHook.KEY_POST_COMMANDS]):
            for command in hook[BaseHook.KEY_POST_COMMANDS]:
                try:
                    self._run_hook_command(command.split(' '))
                except Exception as e:
                    pcprint('Error @ precommit:', colour=RED)
                    pcprint(e)
                    sys.exit(1)

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
        pcprint('running ' + wcolour(' '.join(command), colour=BLUE), colour=GREEN)
        process = run_shell_command(command)
        process.wait()
        print(process)
        # if process.returncode > 0:
        #     print(process.returncode)
        # raise Exception(stdout.decode() + "\n" + stderr.decode())
