from pytempl.code import BaseCodeTool, Editorconfig
from pytempl.core.loggable import Loggable
from pytempl.git.hooks import HooksConfig
from .base import BaseInquire


class InquirePreCommit(BaseInquire):
    _git_tools_list = []

    def __init__(self, logger: Loggable.Logger, git_tools_list: list = None):
        super().__init__(logger)

        self._key = HooksConfig.HOOK_PRE_COMMIT
        self._git_tools_list = git_tools_list if git_tools_list else []

        self._questions = [
            {
                'type': 'confirm',
                'message': 'Do you wish to use {} ?'.format(
                    self.query_anwers(category=BaseCodeTool.CATEGORY_EDITORCONFIG)[0].get('name', 'UNKNOWN')),
                'name': Editorconfig.TOKEN,
                'default': True,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Use built in tools, for code audit?',
                'name': BaseCodeTool.CATEGORY_AUDIT,
                'choices': [
                               {
                                   'name': 'No, I want to have my own configuration.',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseCodeTool.CATEGORY_AUDIT)
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Code Formatter Tool',
                'name': BaseCodeTool.CATEGORY_FORMATTER,
                'choices': self.query_anwers(category=BaseCodeTool.CATEGORY_FORMATTER),
                           # [
                           #     {
                           #         'name': 'Don\'t use formatter',
                           #         'value': None,
                           #     }
                           # ] + self.query_anwers(category=BaseCodeTool.CATEGORY_FORMATTER),
                # 'validate': lambda answer: 'You must choose at least one code formatter.' if answer else True,
                'when': lambda answers: answers.get(BaseCodeTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Code Linter Tool',
                'name': BaseCodeTool.CATEGORY_LINTER,
                'choices': self.query_anwers(category=BaseCodeTool.CATEGORY_LINTER),
                # 'validate': lambda answer: 'You must choose at least one code linter.' if answer else True,
                'when': lambda answers: answers.get(BaseCodeTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code Analyzer Tool',
                'name': BaseCodeTool.CATEGORY_ANALYZER,
                'choices': [
                               {
                                   'name': 'Don\'t use analyzer',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseCodeTool.CATEGORY_ANALYZER),
                # 'validate': lambda answer: 'You must choose at least one code analyzer.' if answer else True,
                'when': lambda answers: answers.get(BaseCodeTool.CATEGORY_AUDIT, None) is None,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code UnitTest Tool',
                'name': BaseCodeTool.CATEGORY_UNITTEST,
                'choices': [
                               {
                                   'name': 'Don\'t use unititest',
                                   'value': None,
                               },
                           ] + self.query_anwers(category=BaseCodeTool.CATEGORY_UNITTEST),
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Additional Lint Tools',
                'name': BaseCodeTool.CATEGORY_LINTER_OTHER,
                'choices': self.query_anwers(category=BaseCodeTool.CATEGORY_LINTER_OTHER)
            },
        ]

    def ask(self):
        super().ask()
        self.answers[BaseCodeTool.CATEGORY_EDITORCONFIG] = BaseCodeTool.CATEGORY_EDITORCONFIG if self.answers.get(
            BaseCodeTool.CATEGORY_EDITORCONFIG, True) else None
        return self

    def query_anwers(self, category: str = ''):
        tools = list(map(lambda klass: klass(), filter(lambda item: item().CATEGORY == category, self._git_tools_list)))
        answers = []
        for tool in tools:
            answers.append({
                'name': tool.config.get('name'),
                'value': tool.TOKEN
            })
        return answers
