from cement import App
from jinja2 import Template

import os
import re
import requests
import time
import shutil
import sys

from pytempl.templ.hooks import Base as BaseHook
from pytempl.output.output import pcprint, wcolour, GREEN, YELLOW, BLUE
from pytempl.templ.utils import str2bool


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

    @staticmethod
    def arguments(klass):
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
            (['--with-{}'.format(klass.TOKEN)],
             {'const': True,
              'default': False,
              'dest': 'skip_{}'.format(klass.TOKEN),
              'help': 'also install `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': str2bool}),
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
    def arguments_skip(klass):
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
            (['--skip-{}'.format(klass.TOKEN)],
             {'const': True,
              'default': False,
              'dest': 'skip_{}'.format(klass.TOKEN),
              'help': 'skip installing `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': str2bool}),
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
        args = self._app.pargs
        config = self._config
        log = self._app.log

        pcprint('checking {} config...'.format(wcolour(self.TOKEN, colour=BLUE, ecolour=GREEN)), colour=GREEN);

        use = not getattr(args, 'skip_{}'.format(self.TOKEN), False) or \
              getattr(args, 'with_{}'.format(self.TOKEN), False)

        if not use:
            pcprint('not used. skipping.', colour=YELLOW)

        self._write_config_files()

        # hook = self._create_hook(klass=PreCommit)
        # self._app.hooks.add_hook(hook_type=Collection.TYPE_PRECOMMIT, hook=hook)

        # print(self._app.hooks.to_dict())

    def _write_config_files(self) -> None:
        args = self._app.pargs
        config = self._config

        reconfig = getattr(args, 'reconfig', False) or getattr(args, 'reconfig_{}'.format(self.TOKEN))

        print('')
        for file in config.get('files').keys():
            if not self.exists(file) or reconfig:
                if self.exists(file):
                    shutil.copy(file, '{}.bak-{}'.format(file, time.time()))
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
