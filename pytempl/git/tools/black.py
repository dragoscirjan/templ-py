import sys

# from pytempl.templ import RED, pcprint
from .base import BaseTool


class Black(BaseTool):
    """
    :see: https://github.com/python/black
    """

    ORDER = BaseTool.ORDER_FORMATTER

    TOKEN = 'black'

    CATEGORY = BaseTool.CATEGORY_FORMATTER

    def _init_config(self):
        self.config.update({
            'files': {
                '.black.toml': 'https://templ-project.github.io/python-configs/.black.toml'
            },
            'hook': 'black --config .black.toml',
            'name': 'Black (https://github.com/python/black)',
            'packages': ['black']
        })

    # def validate(self):
    #     if self._args.with_black is True and (sys.version_info[0] < 3 or sys.version_info[1] < 6):
    #         pcprint('Black requires python 3.6 or higher. Please used `Isort` for python 3.5.', colour=RED)
    #         sys.exit(10)
