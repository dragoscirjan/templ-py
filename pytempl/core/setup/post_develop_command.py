from setuptools.command.develop import develop

from pytempl.core import Loggable
from pytempl.di import DI


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    di = None

    def __init__(self, dist):
        super().__init__(dist)
        self.di = DI()
        Loggable.setup_logger(self.di.logger())

    def run(self):
        self.di.logger().warning('Don\'t forget to run: `<green>pytempl init (--new)</green>` for using `pytempl`.')
        develop.run(self)
