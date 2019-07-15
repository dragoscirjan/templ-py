from PyInquirer import prompt, Separator

class Inquire:

    def query(self):
        return prompt([
            {
                'type': 'confirm',
                'message': 'Do you wish to use Editor Conifg https://editorconfig.org ?',
                'name': 'editorconfig',
                'default': True,
                'value': 'abort',
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Use built in tools, for code audit?',
                'name': 'audit',
                'choices': [
                    {
                        'name': 'No, I want to have my own configuration.',
                        'value': None,
                    },
                    {
                        'name': 'Flake8 http://flake8.pycqa.org/',
                        'value': 'flake8',
                    },
                    {
                        'name': 'Pylama https://github.com/klen/pylama',
                        'value': 'pylama',
                    },
                ],
                'validate': lambda answer: 'You must choose at least one code audit tool.' if len(answer) == 0 else True
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Code Formatter Tool',
                'name': 'formatter',
                'choices': [
                    {
                        'name': 'Don\'t use formatter',
                        'value': None,
                    },
                    {
                        'name': 'Isort https://github.com/timothycrosley/isort',
                        'value': 'isort',
                    },
                    {
                        'disabled': 'Unavailable at this time',
                        'name': 'Black https://github.com/python/black',
                        'value': 'black',
                    },
                ],
                'validate': lambda answer: 'You must choose at least one code frmatter.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get('audit', None) is None,
            },
            {
                'type': 'list',
                'qmark': '?',
                'message': 'Select Code Analizer Tool',
                'name': 'analizer',
                'choices': [
                    {
                        'name': 'Don\'t use formatter',
                        'value': None,
                    },
                    {
                        'name': 'Mccabe https://github.com/PyCQA/mccabe',
                        'value': 'mccabe',
                    },
                    {
                        'disabled': 'Unavailable at this time',
                        'name': 'Radon http://radon.readthedocs.io/en/latest/',
                        'value': 'radon',
                    },
                ],
                'validate': lambda answer: 'You must choose at least one code analizer.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get('audit', None) is None,
            },
            {
                'type': 'checkbox',
                'qmark': '?',
                'message': 'Select Code Linter Tool',
                'name': 'linter',
                'choices': [
                    {
                        'name': 'Don\'t use formatter',
                        'value': None,
                    },
                    {
                        'name': 'Pylint https://www.pylint.org',
                        'value': 'pylint',
                    },
                    {
                        'name': 'PyFlakes https://github.com/PyCQA/pyflakes',
                        'value': 'pyflakes',
                    },
                    {
                        'name': 'pycodestyle https://github.com/PyCQA/pycodestyle',
                        'value': 'pycodestyle',
                    },
                    {
                        'name': 'pydocstyle https://github.com/PyCQA/pydocstyle',
                        'value': 'pydocstyle',
                    },
                    {
                        'name': 'Bandit https://github.com/PyCQA/pyflakes',
                        'value': 'bandit',
                    },
                    {
                        'name': 'MyPy http://mypy-lang.org',
                        'value': 'mypy',
                    },
                ],
                'validate': lambda answer: 'You must choose at least one code linter.' if len(answer) == 0 else True,
                'when': lambda answers: answers.get('audit', None) is None,
            },
            # {
            #     'type': 'list',
            #     'qmark': '?',
            #     'message': 'Select Code Linter Tool',
            #     'name': 'linter',
            #     'choices': [
            #         {
            #             'key': None,
            #             'name': 'Don\'t use formatter'
            #         },
            #         {
            #             'key': 'mccabe',
            #             'name': 'Mccabe https://github.com/PyCQA/mccabe'
            #         },
            #         {
            #             'key': 'radon',
            #             'name': 'Radon http://radon.readthedocs.io/en/latest/',
            #             'disabled': 'Unavailable at this time'
            #         },
            #     ],
            #     'validate': lambda answer: 'You must choose at least one code analizer.' if len(answer) == 0 else True
            # },
        ])
