import sys

from pytempl.templ.hooks import Base


class Init(Base):

    _commands = {}

    def store_command(self, command: str):
        argv = sys.argv[2:]
        argv = list(map(lambda s: s if s.find('--') == 0 else "\"{}\"".format(s), argv))
        argv = list(filter(lambda s: s.find('--reconfig') < 0 and s.find('--silent') <= 0, argv))
        argv = ['--silent'] + argv

        self._commands[command] = 'pytempl {} {}'.format(command, ' '.join(argv))

    def to_dict(self):
        return self._commands
