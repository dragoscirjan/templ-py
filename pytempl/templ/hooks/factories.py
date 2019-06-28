from pytempl.templ.hooks import Base, PreCommit
from pytempl.templ.hooks import Collection


class HookFactory:

    @staticmethod
    def from_dict(data: dict, klass=None) -> Base:
        hook = None
        if issubclass(klass, Base):
            hook = klass()
            if type(klass) == str:
                if klass == 'PreCommit' or klass == Collection.TYPE_PRECOMMIT:
                    hook = PreCommit()

        if hook is None:
            raise Exception('Invalid hook class `{}`'.format(str(klass)))

        hook._pre_commands = getattr(data, 'pre-commands', [])
        hook._commands = getattr(data, 'commands', [])
        hook._post_commands = getattr(data, 'post-commands', [])
        return hook


class CollectionFactory:

    @staticmethod
    def from_dict(data: dict) -> Collection:
        collection = Collection()
        for hook_type in data.keys():
            if hook_type not in Collection.TYPES:
                raise Exception('`{}` hook is invalid.'.format(hook_type))
            collection.add_hook(hook_type, HookFactory.from_dict(data=data[hook_type], klass=hook_type))
        return collection
