from jinja2 import Template

import re
import requests
import sys

from pytempl.core import Loggable
from pytempl.os import file_exists, file_backup, file_write
from pytempl.pip import Pip


class BaseCodeTool(Loggable):
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

    _config = {}
    _args = None
    _logger = None
    _pip = None

    def __init__(self, logger: Loggable.Logger, pip: Pip):
        super().__init__(logger=logger)
        self._pip = pip
        self._init_config()

    def _init_config(self):
        self._config = {
            'ext': ['*.py'],
            'files': {},
            'name': '',
            'packages': [],
            'hook': None,
            'append-pre-commit': None,
            'prepend-pre-commit': None
        }

    @property
    def config(self):
        return self._config

    def run(self):
        self._logger.info('checking {} config...'.format(self._config.get('name', None)))
        self.validate()
        self._write_config_files()
        self._pip.install(packages=self._config.get('packages', []))

    def http_copy(self, url: str, file: str):
        try:
            # session = requests.Session()
            # session.verify = False
            # req = session.get(url, verify=False)
            req = requests.get(url)
            self._logger.debug('Downloading {url} to {file}'.format(url=url, file=file))
            if req.status_code < 200 or req.status_code >= 400:
                raise Exception(req.text)
            file_write(req.text, file)
        except Exception as e:  #pylint: disable=W0703
            self._logger.error('Could not download file {}'.format(url))
            self._logger.error(str(e))
            # sys.exit(req.status_code)

    def http_compile(self, url: str, file: str):
        try:
            req = requests.get(url)
            self._logger.debug('Downloading {url} to {file}'.format(url=url, file=file))
            if req.status_code < 200 or req.status_code >= 400:
                raise Exception(req.text)
            template = Template(req.text)
            file_write(template.render(**{}), file)
        except Exception as e:  #pylint: disable=W0703
            self._logger.error('Could not download file {}'.format(url))
            self._logger.error(str(e))
            # sys.exit(req.status_code)

    def validate(self):
        pass

    def _write_config_files(self) -> None:
        for file, url in self._config.get('files').items():
            if file_exists(file):
                self._logger.debug('Backing up {} file'.format(file))

            match = re.compile('.jinja2$', re.IGNORECASE)
            if re.search(match, url) is None:
                self.http_copy(url=url, file=file)
            else:
                self.http_compile(url=url, file=file)

            self._logger.info('{} written.'.format(file))

class BaseToolReq(BaseCodeTool):
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
    #     ] + BaseCodeTool._arguments(klass=klass)
