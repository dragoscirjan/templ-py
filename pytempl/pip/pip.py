import simplejson

from pytempl.core import Loggable
from pytempl.os import file_exists, file_read, file_write, run_shell_command


class Pip(Loggable):

    _requirements = None
    _requirements_dev = None

    _packages = {
        'dev': [],
        'prod': []
    }

    def install(self, packages: list = []):
        # self.read_dependencies()
        dev = self._packages.get('dev', [])
        if not dev:
            dev = ['-r requirements-dev.txt']

        for package in packages:
            found = False
            for item in self._packages.get('dev', []) + self._packages.get('prod', []):
                if package in item or package == item:
                    found = True
                    break
            if not found:
                self._logger.debug('Adding {package} to {file}'.format(package=package, file=self._requirements_dev))
                dev.append(package)

        if packages:
            run_shell_command('pip install {}'.format(' '.join(packages)), print_output=True, raise_output=True)

        # self.write_dependencies()
        pass

    def read_dependencies(self):
        if file_exists('requirements-dev.txt'):
            self._packages['dev'] = file_read('requirements-dev.txt').split("\n")
        if file_exists('requirements.txt'):
            self._packages['prod'] = file_read('requirements.txt').split("\n")
        self._logger.debug('requirements read: {}'.format(simplejson.dumps(self._packages)))


    def set_requirements(self, value: str):
        self._requirements = value

    def set_requirements_dev(self, value: str):
        self._requirements_dev = value

    def write_dependencies(self):
        self._logger.debug('Writing [{packages}] to {file}'.format(
            packages=', '.join(self._packages.get('dev', [])),
            file=self._requirements_dev
        ))
        file_write(
            "\n".join(self._packages.get('dev', [])),
            self._requirements_dev
        )
        # file_write("\n".join(self._packages.get('prod', [])), self._requirements)
