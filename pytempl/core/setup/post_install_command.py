import os
import sys

from setuptools.command.install import install

from pytempl.core import Loggable
from pytempl.di import DI
from pytempl.os import run_shell_command


class PostInstallCommand(install):
    """Post-installation for production mode."""

    di = None

    def __init__(self, dist):
        super().__init__(dist)
        self.di = DI()
        Loggable.setup_logger(self.di.logger())

    def run(self):
        if self.di.git_hooks_config().exists():
            binary_path = os.path.join(os.path.dirname(sys.executable), 'pytempl')
            run_shell_command(command='{} init'.format(binary_path), print_output=True)
        else:
            self.di.logger().warning('Don\'t forget to run: `<green>pytempl init (--new)</green>` for using `pytempl`.')
        install.run(self)
