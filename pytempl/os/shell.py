import argparse
import subprocess
import sys


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    raise argparse.ArgumentTypeError('Boolean value expected.')

#
# https://www.endpoint.com/blog/2015/01/28/getting-realtime-output-using-python
#

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
                if print_output:
                    sys.stdout.write(output)
                if raise_output:
                    sys.exit(process.returncode)
        if print_output:
            sys.stdout.write(output)
    except subprocess.TimeoutExpired:
        stdout = stderr = b''
        process.kill()
    return process, stdout.decode(), stderr.decode()