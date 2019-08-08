import sys

# from pytempl.templ import RED, pcprint
from pytempl.code.base import BaseCodeTool


class Black(BaseCodeTool):
    """
    :see: https://github.com/python/black
    """

    ORDER = BaseCodeTool.ORDER_FORMATTER

    TOKEN = 'black'

    CATEGORY = BaseCodeTool.CATEGORY_FORMATTER

    def _init_config(self):
        super()._init_config()
        self._config.update({
            'files': {
                '.black.toml': 'https://templ-project.github.io/python-configs/black.toml'
            },
            'hook': 'black --config .black.toml',
            'name': 'Black (https://github.com/python/black)',
            'packages': ['black']
        })

    # def validate(self):
    #     if self._args.with_black is True and (sys.version_info[0] < 3 or sys.version_info[1] < 6):
    #         pcprint('Black requires python 3.6 or higher. Please used `Isort` for python 3.5.', colour=RED)
    #         sys.exit(10)
