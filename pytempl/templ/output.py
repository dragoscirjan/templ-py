import sys

from jinja2 import Template

from .utils import run_shell_command

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def tput_colors():
    process = run_shell_command(['tput colors'])
    if 0 == process.returncode:
        return 8 <= int(process.stdout.read().decode())
    return False


# following from Python cookbook, #475186
def has_colours(stream):
    if tput_colors():
        return True
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False  # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except Exception as e:
        # guess false in case of error
        return False


has_colours = has_colours(sys.stdout)


def wcolour(text, colour=WHITE, ecolour=None, data: dict = None):
    if has_colours:
        if data is None:
            return "\x1b[1;%dm" % (30 + colour) + text + "\x1b[%dm" % (0 if ecolour is None else 30 + ecolour)
        else:
            if isinstance(text, Template):
                return text.render(**data)
            else:
                return Template(text).render(**data)
    else:
        return text


def cprint(text, colour=WHITE):
    sys.stdout.write(wcolour(text, colour=colour) + "\n")


def pcprint(text, colour=WHITE, prefix='>>'):
    sys.stdout.write(('{} {}'.format(prefix, wcolour(text, colour=colour))))
    sys.stdout.write("\n")
