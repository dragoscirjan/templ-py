import argparse
import os
import time
import subprocess


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def file_exists(path: str) -> bool:
    return os.path.isfile(os.path.join(os.getcwd(), path))


def file_write(content: str, path: str) -> None:
    f = open(os.path.join(os.getcwd(), path), 'w')
    f.write(content)
    f.close()


def file_read(path: str) -> str:
    f = open(os.path.join(os.getcwd(), path), 'r')
    return f.read()


def file_copy(src: str, dst: str) -> None:
    file_write(content=file_read(src), path=dst)


def file_backup(src: str) -> None:
    file_copy(src, '{}.bak-{}'.format(src, time.time()))


def run_shell_command(command: list) -> tuple:
    """

    :param command: list
    :return: (stdout, stderr)
    """
    return subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
