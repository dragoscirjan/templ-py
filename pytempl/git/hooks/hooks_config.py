import json
import re

import yaml

from pytempl.core import Loggable
from pytempl.os import file_backup, file_exists, file_read, file_write


class HooksConfig(Loggable):

    # :see https://git-scm.com/docs/githooks
    HOOK_PRE_APPLYPATCH = 'pre-applypatch'
    HOOK_POST_APPLYPATCH = 'post-applypatch'
    HOOK_APPLYPATCH_MSG = 'applypatch-msg'
    HOOK_PRE_COMMIT = 'pre-commit'
    HOOK_PREPARE_COMMIT_MSG = 'prepare-commit-msg'
    HOOK_COMMIT_MSG = 'commit-msg'
    HOOK_POST_COMMIT = 'post-commit'
    HOOK_PRE_REBASE = 'pre-rebase'
    HOOK_POST_CHECKOUT = 'post-checkout'
    HOOK_POST_MERGE = 'post-merge'
    HOOK_PRE_PUSH = 'pre-push'
    HOOK_PRE_RECEIVE = 'pre-receive'
    HOOK_UPDATE = 'update'
    HOOK_POST_RECEIVE = 'post-receive'
    HOOK_POST_UPDATE = 'post-update'
    HOOK_PUSH_TO_CHECKOUT = 'push-to-checkout'
    HOOK_PRE_AUTO_GC = 'pre-auto-gc'
    HOOK_POST_REWRITE = 'post-rewrite'
    HOOK_REBASE = 'rebase'
    HOOK_SEND_EMAIL_VALIDATE = 'sendemail-validate'
    HOOK_FSMONITOR_WATCHMAN = 'fsmonitor-watchman'
    HOOK_PS4_PRE_SUBMIT = 'p4-pre-submit'
    HOOK_POST_INDEX_CHANGE = 'post-index-change'

    KEY_COMMANDS = 'commands'
    KEY_PRE_COMMANDS = 'pre-commands'
    KEY_POST_COMMANDS = 'post-commands'

    CONFIG_FILES = [
        '.pytemplrc.yml',
        '.pytemplrc.yaml',
        '.pytemplrc',
        '.pytemplrc.json',
    ]

    _config = {}

    def exists(self) -> bool:
        """
        Test whether config exists
        :return: bool
        """
        for file in self.CONFIG_FILES:
            if file_exists(file):
                return True
        return False

    def config_file(self) -> str:
        """
        Determine config file name
        :return: str
        """
        for file in self.CONFIG_FILES:
            if file_exists(file):
                return file
        return self.CONFIG_FILES[0]

    def from_dict(self, config: dict):
        self._config = config
        return self

    def read(self):
        config_file = self.config_file()
        self._logger.debug('Detected & reading config file {}'.format(config_file))
        if not re.compile('.json$').search(config_file.lower()):
            # self._config = yaml.load(open(config_file), Loader=yaml.Loader)
            self._config = yaml.safe_load(open(config_file))
        else:
            self._config = json.loads(file_read(config_file))
        return self

    def to_dict(self) -> dict:
        """
        Convert config to dictionary
        :return dict
        """
        return self._config

    def write(self):
        config_file = self.config_file()
        self._logger.debug('Detected & writing config file {}'.format(config_file))
        if file_exists(config_file):
            self._logger.debug('Backing `{}` old file'.format(config_file))
            file_backup(config_file)
        if not re.compile('.json$').search(config_file.lower()):
            yaml.dump(self._config, open(config_file, 'w+'))
        else:
            file_write(content=json.dumps(self.to_dict(), indent=4), path=config_file)

        return self
