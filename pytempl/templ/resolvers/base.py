import re
import sys
from functools import reduce

from cement import App

from pytempl.templ import (BLUE, GREEN, file_exists, file_read, file_write,
                           pcprint, wcolour)
from pytempl.templ.hooks import Base as BaseHook
from pytempl.templ.hooks import Collection as HookCollection
from pytempl.templ.hooks import CollectionFactory as HookCollectionFactory
from pytempl.templ.hooks import Init as InitHook


class Base:

    app = None

    def __init__(self, app: App) -> None:
        self.app = app
        self.hook_collection = HookCollectionFactory.from_file()

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

    def _can_reconfig(self) -> bool:
        """
        --reconfig --reconfig-*
        :return: bool
        """
        args = vars(self.app.pargs)
        for key in args.keys():
            if key.find('reconfig') == 0 and args.get(key, False) is True:
                return True
        return False

    def _check_hook_configured_and_exit(self, hook_type: str = ''):
        if self._can_reconfig():
            return

        collection = self.hook_collection.to_dict()
        if hook_type not in collection.keys():
            return

        pcprint('`{}` hook is already configured.'.format(wcolour(hook_type, colour=BLUE, ecolour=GREEN)), colour=GREEN)
        pcprint('to re-configure, use one of the {} options'.format(wcolour('--reconfigure, --reconfigure-*', colour=BLUE, ecolour=GREEN)), colour=GREEN)
        pcprint('check {} command for more help'.format(wcolour('pytempl precommit-config', colour=BLUE, ecolour=GREEN)), colour=GREEN)
        pcprint('exiting...')
        print('')
        sys.exit(0)

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
            if 'prepend-pre-commit' in config.keys():
                hook.add_pre_command(config.get('prepend-pre-commit', ''))
            if 'append-pre-commit' in config.keys():
                hook.add_post_command(config.get('append-pre-commit', ''))

        if len(args.prepend_pre_commit) > 0:
            for command in args.prepend_pre_commit:
                hook.add_pre_command(command)

        if len(args.append_pre_commit) > 0:
            for command in args.append_pre_commit:
                hook.add_post_command(command)

        return hook

    def _get_hook_extensions(self, hook_type: str) -> list:
        """
        Obtain list of extensions configured in hook config.
        :param hook_type: str
        :return: list
        """
        dikt = self.hook_collection.to_dict()
        if hook_type not in dikt.keys() or 'commands' not in dikt[hook_type].keys():
            return []
        return dikt[hook_type]['commands'].keys()

    def _map_files_by_hook_extensions(self, files_list: list) -> dict:
        """
        Map files with their extensions
        :param files_list: list
        :return: dict
        """
        files = {}
        for ext in self._get_hook_extensions(hook_type=HookCollection.TYPE_PRECOMMIT):
            test = re.compile('\\.' + ext.split('.')[1] + '$', re.IGNORECASE)
            files[ext] = []
            for file in files_list:
                if test.search(file):
                    files[ext].append(file)
        return files

    def _prepare_git_hook(self, hook_type: str, command: str):
        """

        :param hook_type: str
        :param command: str
        :return:
        """
        hook_file = '.git/hooks/{}'.format(hook_type)
        if file_exists(path=hook_file) and not self.app.pargs.reconfig is True:
            return
        content = """#! /bin/bash

pytempl {command}

# exit 1        
""".format(command=command)
        file_write(content=content, path=hook_file)
        pcprint('{} created'.format(wcolour('.git/hooks/{}'.format(hook_type), colour=BLUE, ecolour=GREEN)), colour=GREEN)
        print('')

    def _reconfig(self, klass: BaseHook, tools: list = [], command: str = '') -> None:
        """
        Reconfigure a specific git hook and write the entire hook collection to config file.
        :param klass: class
        :param tools: list
        :param command: str
        :return:
        """
        hook = self._create_hook(tools=tools, klass=klass)
        self.hook_collection.add_hook(hook_type=HookCollection.TYPE_PRECOMMIT, hook=hook, force=True)

        init = self.hook_collection.get_hook(HookCollection.TYPE_INIT)
        if init is None:
            init = InitHook()
        init.store_command(command)
        # collection.add_hook(hook_type=HookCollection.TYPE_INIT, hook=init, force=True)
        self.hook_collection.to_file()

    def _required_packages(self, tools: list) -> list:
        """
        Obtain list of packages requiered
        :param tools:
        :return: list
        """
        required_packages = list(map(lambda tool: tool._config.get('packages', []) if tool.use() else [], tools))
        return list(reduce(lambda a, b: a + b, required_packages, []))
