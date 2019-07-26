from setuptools.command.develop import develop

from pytempl.templ.output import BLUE, GREEN, pcprint, wcolour


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        pcprint('Don\'t forget to run: {} for utilizing pytempl.'.format(
            wcolour('pytempl precommit-config', colour=BLUE, ecolour=GREEN)), colour=GREEN)
        develop.run(self)
