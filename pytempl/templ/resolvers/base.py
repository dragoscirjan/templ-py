from cement import App

from pytempl.templ.hooks import Base as BaseHook, Init as InitHook, Collection, CollectionFactory
from pytempl.templ import file_exists, file_read, pcprint, wcolour, GREEN, BLUE


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

    def _check_required_packages(self, packages: list) -> None:
        """
        :param packages:
        :return:
        """
        packages_in_files = []
        for file in ['requirements.txt', 'requirements-dev.txt']:
            if file_exists(file):
                for line in file_read(file).split("\n"):
                    package = line.split('=')[0].split('>')[0].split('<')[0].strip()
                    packages_in_files.append(package)
        packages_in_files = list(filter(lambda item: len(item) > 0, packages_in_files))

        required_packages = list(filter(lambda item: item not in packages_in_files, packages))
        if len(required_packages) > 0:
            pcprint('some packages are missing from {}'.format(wcolour('requirements-dev.txt', colour=BLUE)), colour=GREEN)
            _run = 'pip install ' + ' '.join(required_packages)
            _add = "\n".join(required_packages)
            pcprint('run {}'.format(wcolour(_run, colour=BLUE)), colour=GREEN)
            pcprint('and add', colour=GREEN)
            pcprint(_add, colour=BLUE)
            pcprint('to {}'.format(wcolour('requirements-dev.txt', colour=BLUE)), colour=GREEN)

    def _create_hook(self, tools: list, klass: BaseHook) -> BaseHook:
        args = self.app.pargs
        hook = klass()

        for tool in tools:
            if tool.use() is False:
                continue

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
        return CollectionFactory.from_file()

    def _reconfig(self, klass: BaseHook, tools: list = [], command: str = '') -> None:
        """
        Reconfigure a specific git hook and write the entire hook collection to config file.
        :param klass: class
        :param tools: list
        :param command: str
        :return:
        """
        hook = self._create_hook(tools=tools, klass=klass)
        collection = self._load_collection()
        collection.add_hook(hook_type=Collection.TYPE_PRECOMMIT, hook=hook, force=True)

        init = collection.get_hook(Collection.TYPE_INIT)
        if init is None:
            init = InitHook()
        init.store_command(command)
        # collection.add_hook(hook_type=Collection.TYPE_INIT, hook=init, force=True)
        collection.to_file()

    def _requires_reconfig(self) -> bool:
        """
        --reconfig --reconfig-*
        :return: bool
        """
        args = vars(self.app.pargs)
        for key in args.keys():
            if key.find('reconfig') == 0 and args.get(key, False) is True:
                return True
        return False
