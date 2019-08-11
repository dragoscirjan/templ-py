from pytempl.core import Loggable
from pytempl.os import file_exists, file_read


class Pip(Loggable):

    _packages = {
        'dev': [],
        'prod': []
    }

    def __init__(self, logger: Loggable.Logger):
        super().__init__(logger=logger)
        self.read_dependencies()

    def install(self, packages: list = []):
        print(self._packages)
        print(packages)

    def read_dependencies(self):
        if file_exists('requirements-dev.txt'):
            self._packages['dev'] = file_read('requirements-dev.txt').split("\n")
        if file_exists('requirements.txt'):
            self._packages['prod'] = file_read('requirements.txt').split("\n")

    def write_dependencies(self):
        pass
