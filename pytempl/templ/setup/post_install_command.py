# import os
# import sys

# from PyInquirer import prompt
from setuptools.command.install import install

from pytempl.templ.output import BLUE, GREEN, pcprint, wcolour

# from pytempl.templ.output import WHITE
# from pytempl.templ.utils import run_shell_command


class PostInstallCommand(install):
    """Post-installation for development mode."""

    def run(self):
        pcprint('Don\'t forget to run: {} for utilizing pytempl.'.format(
            wcolour('pytempl precommit-config', colour=BLUE, ecolour=GREEN)), colour=GREEN)
        # answers = prompt([
        #     {
        #         'type': 'confirm',
        #         'message': 'Should we run {} for you?'.format(wcolour('pytempl precommit-config', colour=BLUE, ecolour=WHITE)),
        #         'name': 'precommit-config',
        #         'default': True,
        #         'value': 'abort',
        #     }
        # ])
        # if answers.get('precommit-config', False):
        #     binary_path = os.path.join(
        #         os.path.dirname(sys.executable),
        #         'pytempl'
        #     )
        #     run_shell_command(command='{} precommit-config'.format(binary_path), print_output=True)
        install.run(self)
