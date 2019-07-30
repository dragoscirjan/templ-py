import json
import logging
import re
import yaml

from pytempl.os import file_exists, file_read, file_write, file_backup


class Config:

    HOOK_APPLYPATCH_MSG = 'applypatch-msg'
    HOOK_COMMIT_MSG = 'commit-msg'
    HOOK_POST_UPDATE = 'post-update'
    HOOK_PRE_APPLYPATCH = 'pre-applypatch'
    HOOK_PRE_COMMIT = 'pre-commit'
    HOOK_PREPARE_COMMIT_MSG = 'prepare-commit-msg'
    HOOK_PRE_PUSH = 'pre-push'
    HOOK_PRE_REBASE = 'pre-rebase'
    HOOK_UPDATE = 'update'

    CONFIG_FILES = [
        '.pytemplrc.yml',
        '.pytemplrc.yaml',
        '.pytemplrc',
        '.pytemplrc.json',
    ]

    _config = {}
    _logger = None

    def __init__(self, logger: logging.Logger):
        self._logger = logger

    def config_file(self):
        for file in self.CONFIG_FILES:
            if file_exists(file):
                return file
        return self.CONFIG_FILES[0]

    def from_dict(self, config: dict):
        self._config = config
        return self

    def read(self) -> dict:
        config_file = self.config_file()
        self._logger.debug('Detected & reading config file {}'.format(config_file))
        if not re.compile('.json$').find(config_file.lower()):
            self._config = yaml.load(open(config_file))
        else:
            self._config = json.loads(file_read(config_file))
        return self

    def to_dict(self) -> dict:
        return self._config

    def write(self):
        config_file = self.config_file()
        self._logger.debug('Detected & writing config file {}'.format(config_file))
        if not re.compile('.json$').find(config_file.lower()):
            file_write(content=json.dumps(self.to_dict(), indent=4), path=config_file)
        else:
            yaml.dump(self._config, open(config_file, 'w+'))
        return self