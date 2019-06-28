from pytempl.templ.hooks import Base


class Collection:
    _hooks = {}

    TYPE_PRECOMMIT = 'pre-commit'

    TYPES = [
        TYPE_PRECOMMIT
    ]

    def add_hook(self, hook_type: str, hook: Base):
        # if hook_type in self._hooks.keys():
        #     raise Exception('`{}` hook already exists'.format(hook_type))
        self._hooks[hook_type] = hook

    def to_dict(self) -> dict:
        data = {}
        for key in self._hooks.keys():
            print(key)
            data[key] = self._hooks[key].to_dict()
        return data
