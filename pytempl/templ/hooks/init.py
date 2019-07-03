import sys

from pytempl.templ.hooks import Base


class Init(Base):

    _init_commands = {}

    def store_command(self, command: str):
        argv = sys.argv[2:]
        argv = list(map(lambda s: s if s.find('--') == 0 else "\"{}\"".format(s), argv))
        argv = list(filter(lambda s: s.find('--reconfig') < 0 and s.find('--silent') <= 0, argv))
        argv = ['--silent'] + argv

        self._init_commands[command] = 'pytempl {command} {argv}'.format(command=command, argv=' '.join(argv))

    def to_dict(self):
        return self._init_commands
