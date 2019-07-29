import argparse
import datetime
import os
import subprocess
import sys
import time


class ShellCommandException(Exception):
    """
    Exception for PreCommit Hook Errors
    """
    time = None

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.time = datetime.datetime.now()


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
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


def run_shell_command(command: str, print_output: bool = False, raise_output: bool = False) -> subprocess.Popen:
    """

    :param command: str
    :return: subprocess.Popen
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = ''
    try:
        stdout, stderr = process.communicate(timeout=1000)
        if print_output or raise_output:
            output = stdout.decode()
            if process.returncode > 0:
                output += "\n"
                output += stderr.decode()
                if raise_output:
                    raise ShellCommandException(output)
        if print_output:
            sys.stdout.write(output)
    except subprocess.TimeoutExpired:
        stdout = stderr = b''
        process.kill()
    return process, stdout.decode(), stderr.decode()
