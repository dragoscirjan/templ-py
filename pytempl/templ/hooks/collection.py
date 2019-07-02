import json
import yaml

from pytempl.templ.hooks import Base
from pytempl.templ.utils import file_exists, file_write


class Collection:
    _hooks = {}

    RC_FILE = '.pytemplrc'
    RC_FILE_JSON = '.pytemplrc.json'
    RC_FILE_YML = '.pytemplrc.yml'
    RC_FILE_YAML = '.pytemplrc.yaml'

    POSSIBLE_FILES = [
        RC_FILE,
        RC_FILE_JSON,
        RC_FILE_YML,
        RC_FILE_YAML,
    ]

    TYPE_PRECOMMIT = 'pre-commit'
    TYPE_INIT = 'init'

    TYPES = [
        TYPE_INIT,

        TYPE_PRECOMMIT
    ]

    def add_hook(self, hook_type: str, hook: Base, force: bool = False) -> None:
        """

        :param hook_type: str
        :param hook: Base
        :param force: bool
        :return: None
        """
        if hook_type in self._hooks.keys() and force is False:
            raise Exception('`{}` hook already exists'.format(hook_type))
        self._hooks[hook_type] = hook

    def get_hook(self, hook_type: str):
        if hook_type in self._hooks.keys():
            return self._hooks.get(hook_type, None)

    def to_dict(self) -> dict:
        data = {}
        for key in self._hooks.keys():
            data[key] = self._hooks[key].to_dict()
        return data

    def to_file(self, path: str = None) -> None:
        found_path = path
        if path is None:
            for path in self.POSSIBLE_FILES:
                if file_exists(path):
                    found_path = path
                    break
        if found_path is None:
            found_path = self.RC_FILE

        if path != self.RC_FILE_JSON:
            yaml.dump(self.to_dict(), open(found_path, 'w+'))
        else:
            file_write(content=json.dumps(self.to_dict(), indent=4), path=found_path)
