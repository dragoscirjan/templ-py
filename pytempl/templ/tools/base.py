import os
import re
import sys

import requests
from cement import App
from jinja2 import Template

from pytempl.templ.output import pcprint, wcolour, GREEN, YELLOW, BLUE
from pytempl.templ.utils import str2bool, file_backup


class Base:
    TOKEN = 'base'

    _config = {}
    _app = None

    def __init__(self, app: App = None):
        self._app = app
        self._config = {
            'ext': ['*.py'] + getattr(app.pargs, 'with_{}_extensions'.format(self.TOKEN), []),
            'files': {},
            'hook': None,
            'name': '',
            'packages': []
        }

    def _arguments(klass):
        return [
            (['--reconfig-{}'.format(klass.TOKEN)],
             {'const': True,
              'default': False,
              'dest': 'reconfig_{}'.format(klass.TOKEN),
              'help': 'reconfigure `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': str2bool}),
            (['--with-{}-extensions'.format(klass.TOKEN)],
             {'default': [],
              'dest': 'with_{}_extensions'.format(klass.TOKEN),
              'help': 'add file extensions to be processed by the `{}` tool. i.e. "--with-{}-extensions *.js *.jsx"'.format(
                  klass.TOKEN, klass.TOKEN),
              'nargs': '+',
              'type': str})
        ]

    @staticmethod
    def arguments(klass) -> list:
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
                   (['--with-{}'.format(klass.TOKEN)],
                    {'const': True,
                     'default': False,
                     'dest': 'with_{}'.format(klass.TOKEN),
                     'help': 'also install `{}` tool.'.format(klass.TOKEN),
                     'nargs': '?',
                     'type': str2bool})
               ] + Base._arguments(klass=klass)

    def exists(self, path: str):
        """
        Determine whether path exists and it's file.
        :param path: str
        :return: bool
        """
        return os.path.isfile(path)

    def http_copy(self, url: str, file: str):
        req = requests.get(url)
        try:
            if req.status_code < 200 or req.status_code >= 300:
                raise Exception(req.text)
            f = open(file, 'w')
            f.write(req.text)
            f.close()
        except Exception as e:
            self._app.log.error('Could not download file {}'.format(url))
            self._app.log.warn(e)
            sys.exit(req.status_code)

    def http_compile(self, url: str, file: str):
        req = requests.get(url)
        if req.sratus_code < 200 or req.status_code >= 300:
            raise Exception(req.text)
        template = Template(req.text)
        f = open(file, 'w')
        f.write(template.render(**self._app.pargs))
        f.close()

    def run(self):
        args = vars(self._app.pargs)

        pcprint('checking {} config...'.format(wcolour(self._config.get('name', None), colour=BLUE, ecolour=GREEN)),
                colour=GREEN)

        if not self.use():
            pcprint('not used. skipping.', colour=YELLOW)
            print('')
            return

        self._write_config_files()

    def use(self) -> bool:
        """
        Test whether tool is used or not
        :return: bool
        """
        args = vars(self._app.pargs)
        return args.get('skip_{}'.format(self.TOKEN), None) is False or \
               args.get('with_{}'.format(self.TOKEN), None) is True

    def validate(self):
        pass

    def _write_config_files(self) -> None:
        args = vars(self._app.pargs)
        config = self._config

        reconfig = args.get('reconfig', False) or args.get('reconfig_{}'.format(self.TOKEN))

        for file in config.get('files').keys():
            if not self.exists(file) or reconfig:
                if self.exists(file):
                    file_backup(file)
                    pcprint('backed up...', colour=YELLOW)

                url = config.get('files').get(file)
                match = re.compile('\.jinja2$', re.IGNORECASE)

                if re.search(match, url) is None:
                    self.http_copy(url=url, file=file)
                else:
                    self.http_compile(url=url, file=file)

                if reconfig:
                    pcprint('reconfigured...', colour=YELLOW)
                pcprint('{} written.'.format(wcolour(file, colour=BLUE, ecolour=GREEN)))
            else:
                pcprint('{} exists. moving on...'.format(wcolour(file, colour=BLUE, ecolour=GREEN)))

        print('')
