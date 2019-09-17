import re
import sys

from pytempl.core.loggable import Loggable
from pytempl.git import Git
from pytempl.git.hooks import HooksConfig
from pytempl.os.shell import run_shell_command
from .base import BaseResolver


class PreCommit(BaseResolver):

    _git = None
    """Git Handler"""

    _hooks_config = None
    """Git Hooks Config"""

    _compiled_config = {}
    """Compiled config object"""

    _hook_type = None
    """Used Git Hook Type"""

    _files = []
    """Files to apply preconfig filters on"""

    _commands = []
    """Compiled commands to run"""

    @staticmethod
    def arguments() -> list:
        return [
            (['--file', '-f'],
             {'default': [],
              'dest': 'files',
              'help': 'Files to lint',
              'nargs': '+',
              'type': str})
        ]

    def __init__(self, logger: Loggable.Logger, hooks_config: HooksConfig, git: Git, args: dict = None):
        super().__init__(logger, args)
        self._git = git
        self._hooks_config = hooks_config
        self._hook_type = HooksConfig.HOOK_PRE_COMMIT

    def run(self):
        self.determine_files().determine_config().compile_commands().process()

    def determine_files(self):
        """
        Determine files to process
        :return:
        """
        self._files = self._args.get('files', [])
        if not self._files:
            self._files = self._git.diff_list_files()
        self._logger.debug('Precommit parsing following files: [{}]'.format(', '.join(self._files)))
        return self

    def determine_config(self):
        self._hooks_config.read()
        return self

    def compile_commands(self):
        """
        Compile commands to run for pre-commit
        :return:
        """
        hook_config = self._hooks_config.to_dict().get(self._hook_type, {})

        for command in hook_config.get(HooksConfig.KEY_PRE_COMMANDS, []):
            self._commands.append((command, ''))

        for pext, commands in hook_config.get(HooksConfig.KEY_COMMANDS, {}).items():
            for file in self._files:
                if re.compile(".{}$".format(pext.split('.')[1]), re.IGNORECASE).search(file):
                    for command in commands:
                        self._commands.append((command, file))

        for command in hook_config.get(HooksConfig.KEY_POST_COMMANDS, []):
            self._commands.append((command, ''))
        return self

    def process(self):
        """
        Process commands
        :return:
        """
        hook_config = self._hooks_config.to_dict().get(self._hook_type, {})
        errors = 0
        for command, file in self._commands:
            status = 'Testing `{} {}`'.format(command, file)
            max_len = 70
            status = re.findall('.{1,'+str(max_len)+'}', status)

            failed = 'Failed'
            passed = 'Passed'

            process, stdout, stderr = run_shell_command(command='{} {}'.format(command, file) if file else command)
            errors += 1 if process.returncode > 0 else 0

            if process.returncode:
                # if len(status + failed) < max_len:
                #     status += '<red>{}</red>'.format(failed.rjust(max_len - len(status), '.'))
                # else:
                #     status += "\n" + '<red>{}</red>'.format(failed.rjust(max_len, '.'))
                # self._logger.warning(status)
                if len(status[-1] + failed) + 3 < max_len:
                    status[-1] += '<red><bold>{}</bold></red>'.format(failed.rjust(max_len - len(status[-1]), '.'))
                else:
                    status.append('<red><bold>{}</bold></red>'.format(failed.rjust(max_len + 3, '.')))
                self._logger.warning("\n".join(status))
                self._logger.info('<fg 90>{}\n{}</fg 90>'.format(stdout, stderr))
                print(process.returncode)

                if not hook_config.get('run-all', None):
                    sys.exit(process.returncode)
            else:
                # if len(status + passed) < max_len:
                #     status += '<green>{}</green>'.format(passed.rjust(max_len - len(status), '.'))
                # else:
                #     status += "\n" + '<green>{}</green>'.format(passed.rjust(max_len, '.'))
                # self._logger.info(status)
                if len(status[-1] + passed) + 3 < max_len:
                    status[-1] += '<green>{}</green>'.format(passed.rjust(max_len - len(status[-1]), '.'))
                else:
                    status.append('<green>{}</green>'.format(passed.rjust(max_len + 3, '.')))
                self._logger.info("\n".join(status))

            if file and process.returncode == 0:
                self._git.add(file=file)

        if errors:
            sys.exit(errors)

        return self
