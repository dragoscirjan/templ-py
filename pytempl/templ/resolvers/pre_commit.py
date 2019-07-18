import sys
import datetime

from pytempl.templ import RED, BLUE, GREEN, YELLOW, pcprint, wcolour, run_shell_command
from pytempl.templ.hooks import Base as BaseHook
from pytempl.templ.hooks import Collection as HookCollection
from .base import Base


class HookCommandException(Exception):
    """
    Exception for PreCommit Hook Errors
    """
    time = None
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.time = datetime.datetime.now()


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

        for command in hook.get(BaseHook.KEY_PRE_COMMANDS, []):
            try:
                self._run_hook_command(command)
            except HookCommandException as e:
                pcprint('Error @ precommit:', colour=RED)
                pcprint(e)
                sys.exit(1)

        ext1 = list(files.keys())
        ext2 = list(hook[BaseHook.KEY_COMMANDS].keys())
        extensions = list(set(ext1 + ext2))
        commands = []
        for ext in extensions:
            for command in hook[BaseHook.KEY_COMMANDS].get(ext, []):
                for file in files.get(ext, []):
                    commands.append((command, file))

        # print(commands)

        for command in commands:
            c, f = command
            try:
                self._run_hook_command(c + ' ' + f)
                self._run_hook_command('git add ' + f)
            except HookCommandException as e:
                pcprint('Error @ precommit of: {}'.format(f, colour=YELLOW), colour=RED)
                pcprint(e)
                sys.exit(1)

        for command in hook.get(BaseHook.KEY_POST_COMMANDS, []):
            try:
                self._run_hook_command(command)
            except HookCommandException as e:
                pcprint('Error @ precommit:', colour=RED)
                pcprint(e)
                sys.exit(1)

        # sys.exit(1)

    def _get_precommit_hook(self) -> dict:
        """

        :return: dict
        """
        return self.hook_collection.get_hook(hook_type=HookCollection.TYPE_PRECOMMIT).to_dict()

    @staticmethod
    def _get_changed_precommit_files() -> list:
        """
        Get list of files de
        :return: list
        """
        process = run_shell_command('git diff --cached --name-only')
        if process.returncode > 0:
            if process.stderr:
                pcprint(process.stderr.read().decode(), colour=RED)
            return []
        return process.stdout.read().decode().split("\n")

    @staticmethod
    def _run_hook_command(command: list) -> None:
        """

        :param command:
        :return:
        """
        pcprint('running ' + wcolour(command, colour=BLUE), colour=GREEN)
        process = run_shell_command(command)
        if process.returncode > 0:
            output = ''
            if process.stdout:
                output += process.stdout.read().decode()
            if process.stderr:
                if output:
                    output += "\n"
                output += process.stderr.read().decode()
            raise HookCommandException(output)
