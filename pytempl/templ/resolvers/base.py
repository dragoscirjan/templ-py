from cement import App

from pytempl.templ.hooks import Base as BaseHook, Collection
from pytempl.templ import file_exists, file_read


class Base:

    app = None

    def __init__(self, app: App) -> None:
        self.app = app

    @staticmethod
    def arguments() -> list:
        """
        Return the list of arguments for a certain command
        :return: list
        """
        return []

    def run(self) -> None:
        """
        Command resolve
        :return:
        """
        pass

    def _create_hook(self, tools: list, klass: BaseHook) -> BaseHook:
        args = self.app.pargs
        hook = klass()

        for tool in tools:
            config = tool._config
            commands = config.get('hook', None)
            extensions = config.get('ext', None)

            if type(commands) == str:
                for ext in extensions:
                    hook.add_command(command=commands, ext=ext)
            if type(commands) == list:
                for ext in extensions:
                    for command in commands:
                        hook.add_command(command=command, ext=ext)

        if len(args.prepend_pre_commit) > 0:
            for command in args.prepend_pre_commit:
                hook.add_pre_command(command)

        if len(args.append_pre_commit) > 0:
            for command in args.append_pre_commit:
                hook.add_post_command(command)

        return hook

    def _load_collection(self) -> Collection:
        # collection = CollectionFactory.from_file()
        collection = Collection()
        return collection

    def _check_packages(self, packages: list) -> None:
        already_in_list = []
        for file in ['requirements.txt', 'requirements-dev.txt']:
            if file_exists(file):
                for line in file_read(file).split("\n"):
                    package = line.split('=')[0].split('>')[0].split('<')[0].strip()
                    already_in_list.append(package)
        print(already_in_list)
