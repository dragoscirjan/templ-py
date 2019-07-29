import sys

from pytempl.templ import BLUE, GREEN, RED, ShellCommandException, pcprint, run_shell_command, wcolour
from pytempl.templ.hooks import Base as BaseHook
from pytempl.templ.hooks import Collection as HookCollection
from .base import Base


class PreCommit(Base):

    @staticmethod
    def arguments() -> list:
        return [
            (['--file', '-f'],
             {'default': [],
              'dest': 'files',
              'help': 'Files to pass through `precommit` checks',
              'nargs': '+',
              'type': str})
        ]

    def run(self) -> None:
        """
        Command Resolver for precommit Command
        :return: None
        """
        hook = self._get_precommit_hook()
        if not self.app.pargs.files:
            files_list = self._get_changed_precommit_files()
        else:
            files_list = self.app.pargs.files
        files = self._map_files_by_hook_extensions(files_list=files_list)
        commands = []
        # errors = []

        for command in hook.get(BaseHook.KEY_PRE_COMMANDS, []):
            commands.append((command, False))

        ext1 = list(files.keys())
        ext2 = list(hook[BaseHook.KEY_COMMANDS].keys())
        extensions = list(set(ext1 + ext2))
        for ext in extensions:
            for command in hook[BaseHook.KEY_COMMANDS].get(ext, []):
                for file in files.get(ext, []):
                    commands.append((command, file))

        for command in hook.get(BaseHook.KEY_POST_COMMANDS, []):
            commands.append((command, False))

        for command in commands:
            c, f = command
            try:
                if f:
                    self. _run_hook_command(c + ' ' + f)
                    if not self.app.pargs.files:
                        self._run_hook_command('git add ' + f)
                else:
                    self. _run_hook_command(c)
            except ShellCommandException as e:
                sys.stdout.write(str(e))
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
        process, stdout, stderr = run_shell_command('git diff --cached --name-only')
        if process.returncode > 0:
            if stderr:
                pcprint(stderr, colour=RED)
            return []
        return stdout.split("\n")

    @staticmethod
    def _run_hook_command(command: str) -> None:
        """

        :param command: str
        :return: None
        """
        pcprint('running ' + wcolour(command, colour=BLUE), colour=GREEN)
        run_shell_command(command=command, print_output=False, raise_output=True)
