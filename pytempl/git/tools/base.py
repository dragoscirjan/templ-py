# import os
# import re
# import sys

# import requests
# from cement import App
# from jinja2 import Template

# # from pytempl.templ.output import BLUE, GREEN, YELLOW, pcprint, wcolour
# from pytempl.templ.utils import file_backup, str2bool


class BaseTool:
    TOKEN = 'base'

    CATEGORY_AUDIT = 'audit'
    CATEGORY_ANALYZER = 'analyzer'
    CATEGORY_EDITORCONFIG = 'editorconfig'
    CATEGORY_FORMATTER = 'formatter'
    CATEGORY_LINTER = 'linter'
    CATEGORY_LINTER_OTHER = 'linter_other'
    CATEGORY_UNITTEST = 'unittest'

    CATEGORIES = [
        CATEGORY_AUDIT,
        CATEGORY_ANALYZER,
        CATEGORY_EDITORCONFIG,
        CATEGORY_FORMATTER,
        CATEGORY_LINTER,
        CATEGORY_LINTER_OTHER,
        CATEGORY_UNITTEST,
    ]

    ORDER_AUDIT = 1
    ORDER_ANALYZER = 50
    ORDER_EDITORCONFIG = 1
    ORDER_FORMATTER = 10
    ORDER_LINTER = 30
    ORDER_LINTER_OTHER = 31
    ORDER_UNITTEST = 90

    config = {}
    
    _args = None

    # def __init__(self, app: App = None):
    def __init__(self):
        # self._args = vars(app.pargs)
        self._init_config()

    def _init_config(self):
        self.config = {
            'ext': ['*.py'],
            'files': {},
            'hook': None,
            'name': '',
            'packages': []
        }

    # @staticmethod
    # def _arguments(klass):
    #     return [
    #         (['--reconfig-{}'.format(klass.TOKEN)],
    #          {'const': True,
    #           'default': False,
    #           'dest': 'reconfig_{}'.format(klass.TOKEN),
    #           'help': 'reconfigure `{}` tool.'.format(klass.TOKEN),
    #           'nargs': '?',
    #           'type': str2bool}),
    #         (['--with-{}-extensions'.format(klass.TOKEN)],
    #          {'default': [],
    #           'dest': 'with_{}_extensions'.format(klass.TOKEN),
    #           'help': 'add file extensions to be processed by the `{}` tool. i.e. "--with-{}-extensions *.js *.jsx"'.format(
    #               klass.TOKEN, klass.TOKEN),
    #           'nargs': '+',
    #           'type': str})
    #     ]

    # @staticmethod
    # def arguments(klass) -> list:
    #     """
    #     Obtain list of arguments for tool
    #     :param klass: class to build arguments for
    #     :return:
    #     """
    #     return [
    #         (['--with-{}'.format(klass.TOKEN)],
    #          {'const': True,
    #           'default': False,
    #           'dest': 'with_{}'.format(klass.TOKEN),
    #           'help': 'also install `{}` tool.'.format(klass.TOKEN),
    #           'nargs': '?',
    #           'type': str2bool})
    #     ] + BaseTool._arguments(klass=klass)

    # @staticmethod
    # def exists(path: str):
    #     """
    #     Determine whether path exists and it's file.
    #     :param path: str
    #     :return: bool
    #     """
    #     return os.path.isfile(path)

    # def http_copy(self, url: str, file: str):
    #     headers = {
    #         'Accept': 'application/vnd.github.v3.raw'
    #     }
    #     if os.getenv('GITHUB_TOKEN', None):
    #         headers['Authorization'] = 'token {}'.format(os.getenv('GITHUB_TOKEN', None))

    #     req = requests.get(url)

    #     try:
    #         if req.status_code < 200 or req.status_code >= 300:
    #             raise Exception(req.text)
    #         f = open(file, 'w')
    #         f.write(req.text)
    #         f.close()
    #     except Exception as e:  #pylint: disable=W0703
    #         self._app.log.error('Could not download file {}'.format(url))
    #         self._app.log.warn(e)
    #         sys.exit(req.status_code)

    # def http_compile(self, url: str, file: str):
    #     headers = {
    #         'Accept': 'application/vnd.github.v3.raw'
    #     }
    #     if os.getenv('GITHUB_TOKEN', None):
    #         headers['Authorization'] = 'token {}'.format(os.getenv('GITHUB_TOKEN', None))

    #     req = requests.get(url, headers=headers)

    #     if req.sratus_code < 200 or req.status_code >= 300:
    #         raise Exception(req.text)

    #     template = Template(req.text)
    #     f = open(file, 'w')
    #     f.write(template.render(**self._app.pargs))
    #     f.close()

    # def run(self):
    #     # args = vars(self._app.pargs)

    #     pcprint('checking {} config...'.format(wcolour(self.config.get('name', None), colour=BLUE, ecolour=GREEN)),
    #             colour=GREEN)

    #     if not self.use():
    #         pcprint('not used. skipping.', colour=YELLOW)
    #         print('')
    #         return

    #     self._write_config_files()

    # def use(self) -> bool:
    #     """
    #     Test whether tool is used or not
    #     :return: bool
    #     """
    #     args = vars(self._app.pargs)
    #     return args.get('skip_{}'.format(self.TOKEN), None) is False or \
    #         args.get('with_{}'.format(self.TOKEN), None) is True

    # def validate(self):
    #     pass

    # def _write_config_files(self) -> None:
    #     args = vars(self._app.pargs)
    #     config = self.config

    #     reconfig = args.get('reconfig', False) or args.get('reconfig_{}'.format(self.TOKEN))

    #     for file in config.get('files').keys():
    #         if not self.exists(file) or reconfig:
    #             if self.exists(file):
    #                 file_backup(file)
    #                 pcprint('backed up...', colour=YELLOW)

    #             url = config.get('files').get(file)
    #             match = re.compile('.jinja2$', re.IGNORECASE)

    #             if re.search(match, url) is None:
    #                 self.http_copy(url=url, file=file)
    #             else:
    #                 self.http_compile(url=url, file=file)

    #             if reconfig:
    #                 pcprint('reconfigured...', colour=YELLOW)
    #             pcprint('{} written.'.format(wcolour(file, colour=BLUE, ecolour=GREEN)))
    #         else:
    #             pcprint('{} exists. moving on...'.format(wcolour(file, colour=BLUE, ecolour=GREEN)))

    #     print('')

class BaseToolReq(BaseTool):
    pass    
    # @staticmethod
    # def arguments(klass) -> list:
    #     """
    #     Obtain list of arguments for tool
    #     :param klass: class to build arguments for
    #     :return:
    #     """
    #     return [
    #         (['--skip-{}'.format(klass.TOKEN)],
    #          {'const': True,
    #           'default': False,
    #           'dest': 'skip_{}'.format(klass.TOKEN),
    #           'help': 'skip installing `{}` tool.'.format(klass.TOKEN),
    #           'nargs': '?',
    #           'type': str2bool})
    #     ] + BaseTool._arguments(klass=klass)
