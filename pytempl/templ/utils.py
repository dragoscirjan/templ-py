import argparse
import os
import time
import shutil


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
    return os.path.isfile(path)


def file_write(content: str, path: str) -> None:
    f = open(path, 'w')
    f.write(content)
    f.close()


def file_read(path: str) -> str:
    f = open(path, 'r')
    return f.read()

def file_copy(src: str, dst: str) -> None:
    shutil.copy(src, dst)

def file_backup(src: str) -> None:
    file_copy(src, '{}.bak-{}'.format(src, time.time()))
