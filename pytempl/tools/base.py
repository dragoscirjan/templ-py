from cement import App


from jinja2 import Template
import os
import requests
import sys


class Base:
    TOKEN = 'base'

    _config = {}
    _app = None

    def __init__(self, app: App = None):
        self._app = app
        self._config = {
            'packages': [],
            'files': {},
            'ext': ['*.py'] + getattr(app.pargs, 'with_{}_extensions'.format(self.TOKEN), []),
            'hook': None
        }

    @staticmethod
    def arguments(klass):
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
            (['--skip-{}'.format(klass.TOKEN)],
             {'default': False,
              'dest': 'skip_{}'.format(klass.TOKEN),
              'help': 'skip installing `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': bool}),
            (['--reconfig-{}'.format(klass.TOKEN)],
             {'default': False,
              'dest': 'reconfig_{}'.format(klass.TOKEN),
              'help': 'reconfigure `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': bool}),
            (['--with-{}-extensions'.format(klass.TOKEN)],
             {'default': [],
              'dest': 'with_{}_extensions'.format(klass.TOKEN),
              'help': 'add file extensions to be processed by the `{}` tool. i.e. "--with-{}-extensions *.js *.jsx"'.format(
                  klass.TOKEN, klass.TOKEN),
              'nargs': '+',
              'type': str})
        ]

    @staticmethod
    def arguments_with(klass):
        """
        Obtain list of arguments for tool
        :param klass: class to build arguments for
        :return:
        """
        return [
            (['--with-{}'.format(klass.TOKEN)],
             {'default': False,
              'dest': 'skip_{}'.format(klass.TOKEN),
              'help': 'also install `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': bool}),
            (['--reconfig-{}'.format(klass.TOKEN)],
             {'default': False,
              'dest': 'reconfig_{}'.format(klass.TOKEN),
              'help': 'reconfigure `{}` tool.'.format(klass.TOKEN),
              'nargs': '?',
              'type': bool}),
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

    def copy(self, url: str, file: str):
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

    # def compile(self, url: str, file: str):
    #     req = requests.get(url)
    #     if req.sratus_code < 200 or req.status_code >= 300:
    #         raise Exception(req.text)
    #     template = Template(req.text)
    #     f = open(file, 'w')
    #     f.write(template.render(**self._app.pargs))
    #     f.close()

    def run(self):
        args = self._app.pargs
        config = self._config
        log = self._app.log


        log.info('checking {} config ...'.format(self.TOKEN));

        use = not getattr(args, 'skip_{}'.format(self.TOKEN), False) or \
              getattr(args, 'with_{}'.format(self.TOKEN), False)

        if not use:
            log.warn('not used. skipping.')

        reconfig = getattr(args, 'reconfig', False) or getattr(args, 'reconfig_{}'.format(self.TOKEN))

        log.info('')

        for file in config.get('files').keys():
            if not self.exists(file) or reconfig:
                self.copy(url=config.get('files').get(file), file=file)
                if reconfig:
                    log.warn('reconfiguring...')
                log.info('{} written.'.format(file))
            else:
                log.info('{} exists. moving on...'.format(file))

    # const staged = {};
    #
    # for (let tool of this.tools) {
    #   this.log(`checking ${chalk.green(tool.title)} config ...`);
    #   if (!tool.use) {
    #     this.log('not used. skipping');
    #     this.isLoud && super.log('');
    #     continue;
    #   }
    #
    #   if (tool.files) {
    #     for (let file in tool.files) {
    #       if (!exists(file) || tool.reconfig) {
    #         write(file, await read(tool.files[file]));
    #         if (tool.reconfig) {
    #           this.log(chalk.yellow('reconfiguring...'));
    #         }
    #         this.log(`${chalk.green(file)} written.`);
    #       } else {
    #         this.log(`${chalk.green(file)} exists. moving on...`);
    #       }
    #     }
    #   }
    #
    #   for (let ext of (tool.ext || []).filter(e => e.trim())) {
    #     if (tool.hook) {
    #       staged[ext] = staged[ext] || [];
    #       for (let hook of Array.isArray(tool.hook) ? tool.hook : [tool.hook]) {
    #         staged[ext].push(hook);
    #       }
    #     }
    #   }
    #
    #   for (let message of this.messages[tool.token] || []) {
    #     this.log(message);
    #   }
    #   this.isLoud && super.log('');
    # }
    #
    # this.configurePackagesJson(flags, staged);
    # this.log('done');
    # this.isLoud && super.log('');
