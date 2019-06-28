

class Base:

    KEY_COMMANDS = 'commands'
    KEY_PRE_COMMANDS = 'pre-commands'
    KEY_POST_COMMANDS = 'post-commands'

    _pre_commands = []
    _commands = {}
    _post_commands = []

    def add_command(self, command: str, ext: str = '*.py'):
        if not ext in self._commands.keys():
            self._commands[ext] = []
        self._commands[ext].append(command)

    def add_pre_command(self, command: str):
        self._pre_commands.append(command)

    def add_post_command(self, command: str):
        self._post_commands.append(command)

    def to_dict(self):
        return {
            self.KEY_PRE_COMMANDS: self._pre_commands,
            self.KEY_COMMANDS: self._commands,
            self.KEY_POST_COMMANDS: self._post_commands
        }
