from .base import BaseInquire
from pytempl.git.hooks.hooks_config import HooksConfig


class InquireHooks(BaseInquire):

    _questions = {
        'type': 'checkbox',
        'qmark': '?',
        'message': 'Select Hooks to Configure:',
        'name': 'hooks',
        'choices': [
            {
                'name': '({}) - run before commit'.format(HooksConfig.HOOK_PRE_COMMIT),
                'value': HooksConfig.HOOK_PRE_COMMIT,
            },
        ],
        'validate': lambda answer: 'You must choose at least one hook.' if len(answer) == 0 else True,
    }