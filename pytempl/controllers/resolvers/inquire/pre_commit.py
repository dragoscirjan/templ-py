from .base import BaseInquire
from pytempl.git.hooks.hooks_config import HooksConfig
from pytempl.git.tools import active_precommit_tools, Editorconfig


class InquirePreCommit(BaseInquire):

    def __init__(self):
        self._questions = [
            {
                'type': 'confirm',
                'message': 'Do you wish to use EditorConifg https://editorconfig.org ?',
                'name': Editorconfig.TOKEN,
                'default': True,
                'value': 'abort',
            },
            # {
            #     'type': 'list',
            #     'qmark': '?',
            #     'message': 'Use built in tools, for code audit?',
            #     'name': BaseTool.CATEGORY_AUDIT,
            #     'choices': [
            #                    {
            #                        'name': 'No, I want to have my own configuration.',
            #                        'value': None,
            #                    },
            #                ] + self.query_anwers(category=BaseTool.CATEGORY_AUDIT),
            #     'validate': lambda answer: 'You must choose at least one code audit tool.' if len(answer) == 0 else True
            # },
            # {
            #     'type': 'list',
            #     'qmark': '?',
            #     'message': 'Select Code Formatter Tool',
            #     'name': BaseTool.CATEGORY_FORMATTER,
            #     'choices': [
            #                    {
            #                        'name': 'Don\'t use formatter',
            #                        'value': None,
            #                    }
            #                ] + self.query_anwers(category=BaseTool.CATEGORY_FORMATTER),
            #     'validate': lambda answer: 'You must choose at least one code formatter.' if len(answer) == 0 else True,
            #     'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            # },
            # {
            #     'type': 'checkbox',
            #     'qmark': '?',
            #     'message': 'Select Code Linter Tool',
            #     'name': BaseTool.CATEGORY_LINTER,
            #     'choices': self.query_anwers(category=BaseTool.CATEGORY_LINTER),
            #     'validate': lambda answer: 'You must choose at least one code linter.' if len(answer) == 0 else True,
            #     'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            # },
            # {
            #     'type': 'list',
            #     'qmark': '?',
            #     'message': 'Select Code Analizer Tool',
            #     'name': BaseTool.CATEGORY_ANALYZER,
            #     'choices': [
            #                    {
            #                        'name': 'Don\'t use formatter',
            #                        'value': None,
            #                    },
            #                ] + self.query_anwers(category=BaseTool.CATEGORY_ANALYZER),
            #     'validate': lambda answer: 'You must choose at least one code analyzer.' if len(answer) == 0 else True,
            #     'when': lambda answers: answers.get(BaseTool.CATEGORY_AUDIT, None) is None,
            # },
            # {
            #     'type': 'list',
            #     'qmark': '?',
            #     'message': 'Select Code UnitTest Tool',
            #     'name': BaseTool.CATEGORY_UNITTEST,
            #     'choices': [
            #                    {
            #                        'name': 'Don\'t use unititest',
            #                        'value': None,
            #                    },
            #                ] + self.query_anwers(category=BaseTool.CATEGORY_UNITTEST),
            # },
            # {
            #     'type': 'checkbox',
            #     'qmark': '?',
            #     'message': 'Select Additional Lint Tools',
            #     'name': BaseTool.CATEGORY_LINTER_OTHER,
            #     'choices': self.query_anwers(category=BaseTool.CATEGORY_LINTER_OTHER)
            # },
        ]

    def query_anwers(self, category: str = ''):
        klasses = list(filter(lambda item: item.CATEGORY == category, active_precommit_tools))
        answers = []
        for klass in klasses:
            answers.append({
                'name': klass(self.app)._config.get('name'),
                'value': klass.TOKEN
            })
        return answers
