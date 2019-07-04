from .base import Base

from pytempl.templ.hooks import CollectionFactory as HookCollectionFactory, Collection as HookCollection
from pytempl.templ import run_shell_command


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

        files = self._get_changed_added_files()

        print(hook, files)

    def _get_changed_added_files(self) -> list:
        """

        :return: list
        """
        stdout, stderr = run_shell_command(['git', 'diff', '--cached', '--name-only'])
        if stderr is not None:
            # TODO: show error message
            pass
        return stdout.decode().split("\n")

    def _get_precommit_hook(self) -> dict:
        """

        :return: dict
        """
        return self.hook_collection.to_dict()[HookCollection.TYPE_PRECOMMIT]
