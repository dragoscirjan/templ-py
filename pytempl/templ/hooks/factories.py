import json

import yaml

from pytempl.templ.hooks import Base, Init, PreCommit, Collection
from pytempl.templ.utils import file_read, file_exists


class HookFactory:

    @staticmethod
    def from_dict(data: dict, klass=None) -> Base:
        """

        :param data: dict
        :param klass: class
        :return: Base
        """
        hook = None

        if type(klass) == str:
            if klass == 'PreCommit' or klass == Collection.TYPE_PRECOMMIT:
                hook = PreCommit()
            if klass == 'Init' or klass == Collection.TYPE_INIT:
                hook = Init()
        else:
            if issubclass(klass, Base):
                hook = klass()

        if hook is None:
            raise Exception('Invalid hook class `{}`'.format(str(klass)))

        hook._pre_commands = data.get('pre-commands', [])
        hook._commands = data.get('commands', [])
        hook._post_commands = data.get('post-commands', [])
        return hook


class CollectionFactory:

    @staticmethod
    def from_dict(data: dict) -> Collection:
        """

        :param data: dict
        :return: Collection
        """
        collection = Collection()
        for hook_type in data.keys():
            if hook_type not in Collection.TYPES:
                raise Exception('`{}` hook is invalid.'.format(hook_type))
            collection.add_hook(hook_type=hook_type, hook=HookFactory.from_dict(data=data[hook_type], klass=hook_type),
                                force=True)
        return collection

    @staticmethod
    def from_file(path: str = None) -> Collection:
        """

        :param path: str
        :return: Collection
        """
        found_path = None

        if path is None:
            for path in Collection.POSSIBLE_FILES:
                if file_exists(path):
                    found_path = path
                    break
        else:
            found_path = path

        if found_path is None:
            return Collection()

        text_data = file_read(found_path)

        if len(text_data) == 0:
            return CollectionFactory.from_dict(data={})

        try:
            data = json.loads(text_data)
        except Exception as e:
            if found_path == Collection.RC_FILE_JSON:
                raise e
            data = yaml.safe_load(text_data)

        return CollectionFactory.from_dict(data=data)
