from functools import reduce

from cement import App
from PyInquirer import prompt

from pytempl.templ import BLUE, GREEN, pcprint, wcolour
from pytempl.templ.hooks import Collection as HookCollection
from pytempl.templ.hooks import PreCommit as PreCommitHook
from pytempl.templ.resolvers import Base as BaseResolver
from pytempl.templ.tools import Base as BaseTool
from pytempl.templ.tools import BaseReq as BaseReqTool
from pytempl.templ.tools import Editorconfig, active_precommit_tools
from pytempl.templ.utils import run_shell_command, str2bool


class PreCommitConfig(BaseResolver):

    @staticmethod
    def arguments() -> list:
        """
        Obtain List of Arguments for precommit-config Command
        :return: list
        """
        return [
                   (['--interactive'],
                    {'const': True,
                     'default': False,
                     'dest': 'interactive',
                     'help': 'Run configure with interactive wizzard.',
                     'nargs': '?',
                     'type': str2bool}),
                   (['--reconfig'],
                    {'const': True,
                     'default': False,
                     'dest': 'reconfig',
                     'help': 'Reconfigure all installed tools.',
                     'nargs': '?',
                     'type': str2bool}),
                   (['--silent'],
                    {'const': True,
                     'default': False,
                     'dest': 'silent',
                     'help': 'Silent run. Logging is disabled.',
                     'nargs': '?',
                     'type': str2bool}),
                   (['--append-pre-commit'],
                    {'default': [],
                     'dest': 'append_pre_commit',
                     'help': 'Add custom pre-commit command at beggining of list.',
                     'nargs': '+',
                     'type': str}),
                   (['--prepend-pre-commit'],
                    {'default': [],
                     'dest': 'prepend_pre_commit',
                     'help': 'Add custom pre-commit command at end of list.',
                     'nargs': '+',
                     'type': str})
               ] + reduce((lambda a, b: a + b), [klass.arguments(klass) for klass in active_precommit_tools])

    def __init__(self, app: App) -> None:
        """
        :param app: App
        """
        super().__init__(app)
        self.hook = self.hook_collection.get_hook(hook_type=HookCollection.TYPE_PRECOMMIT)

    def query_anwers(self, category: str = ''):
        klasses = list(filter(lambda item: item.CATEGORY == category, active_precommit_tools))
        answers = []
        for klass in klasses:
            answers.append({
                'name': klass(self.app)._config.get('name'),
                'value': klass.TOKEN
            })
        return answers

    def query(self):
        """

        :return: list
        """
        return prompt([
            {
                'type': 'confirm',
                'message': 'Do you wish to use EditorConifg https://editorconfig.org ?',
                'name': Editorconfig.TOKEN,
                'default': True,
                'value': 'abort',
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Use built in tools, for code audit?',
                'name': BaseTool.CATEGORY_AUDIT,
                'choices': [
                               {
                                   'name': 'No, I want to have my own configuration.',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseTool.CATEGORY_AUDIT),
                'validate': lambda answer: 'You must choose at least one code audit tool.' if len(answer) == 0 else True
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code Formatter Tool',
                'name': BaseTool.CATEGORY_FORMATTER,
                'choices': [
                               {
                                   'name': 'Don\'t use formatter',
                                   'value': None,
                               }
                           ] + self.query_anwers(category=BaseTool.CATEGORY_FORMATTER),
                'validate': lambda answer: 'You must choose at least one code formatter.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Code Linter Tool',
                'name': BaseTool.CATEGORY_LINTER,
                'choices': self.query_anwers(category=BaseTool.CATEGORY_LINTER),
                'validate': lambda answer: 'You must choose at least one code linter.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code Analizer Tool',
                'name': BaseTool.CATEGORY_ANALYZER,
                'choices': [
                               {
                                   'name': 'Don\'t use formatter',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseTool.CATEGORY_ANALYZER),
                'validate': lambda answer: 'You must choose at least one code analyzer.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code UnitTest Tool',
                'name': BaseTool.CATEGORY_UNITTEST,
                'choices': [
                               {
                                   'name': 'Don\'t use unititest',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseTool.CATEGORY_UNITTEST),
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Additional Lint Tools',
                'name': BaseTool.CATEGORY_LINTER_OTHER,
                'choices': self.query_anwers(category=BaseTool.CATEGORY_LINTER_OTHER)
            },
        ])

    def query_to_command(self, answers):
        """
        Compose command
        :param answers: dict
        :return: str
        """
        command = ''
        answers_keys = answers.keys()
        for category in BaseTool.CATEGORIES:
            if category == BaseTool.CATEGORY_EDITORCONFIG and answers.get(category, False) is False:
                command = command + ' --skip-{}'.format(BaseTool.CATEGORY_EDITORCONFIG)
            else:
                answer_values = answers.get(category, [])
                answer_values = answer_values if type(answer_values) == list else [answer_values]
                if category in answers_keys and len(answer_values) > 0:
                    for klass in list(filter(lambda item: item.CATEGORY == category, active_precommit_tools)):
                         if issubclass(klass, BaseTool) and not issubclass(klass,
                                                                          BaseReqTool) and klass.TOKEN in answer_values:
                            command = command + ' --with-{}'.format(klass.TOKEN)
                else:
                    for klass in list(filter(lambda item: item.CATEGORY == category, active_precommit_tools)):
                         if issubclass(klass, BaseReqTool) and klass.TOKEN not in answer_values:
                            command = command + ' --skip-{}'.format(klass.TOKEN)
        return 'pytempl precommit-config' + command

    def run(self) -> None:
        """
        Command Resolver for precommit-config Command
        :return: None
        """

        if (self.app.pargs.interactive):
            answers = self.query()
            pcprint('Thankyou for stating your options.', colour=GREEN)
            pcprint('Running compiled command: {}'.format(
                wcolour(self.query_to_command(answers), colour=BLUE)
            ), colour=GREEN)
            process, stdout, stderr = run_shell_command(self.query_to_command(answers))
            if stderr:
                print(stderr)
            else:
                print(stdout)
            return

        self._prepare_git_hook(hook_type=HookCollection.TYPE_PRECOMMIT, command='precommit')

        self._check_hook_configured_and_exit(hook_type=HookCollection.TYPE_PRECOMMIT)

        tools = self._init_tools()
        required_packages = self._required_packages(tools)

        for tool in tools:
            tool.run()

        if self._can_reconfig():
            self._reconfig(klass=PreCommitHook, tools=tools, command='precommit')

        # TODO: Should be presented only at config action is taken
        self._check_required_packages(packages=required_packages)

    def _init_tools(self) -> list:
        """
        Initialize `pytempl.templ.tools`
        :return: list
        """
        tools = []
        for klass in active_precommit_tools:
            tool = klass(app=self.app)
            tool.validate()
            tools.append(tool)
        return tools
