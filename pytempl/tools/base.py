

class Base:

    TOKEN = 'base'

    _config = {}

    def __init__(self):
        self._config = {
            packages: [],
            files: {},
            ext: ['*.py'],
            hook: None
        }