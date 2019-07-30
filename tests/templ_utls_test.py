"""
PyTest Fixtures.
"""

import argparse

from pytempl.templ.utils import ShellCommandException, run_shell_command, str2bool

# import pytest



def test_str2bool():
    assert str2bool(True) is True
    assert str2bool('true') is True
    assert str2bool('TRUE') is True
    assert str2bool('1') is True
    assert str2bool('yes') is True
    assert str2bool('y') is True
    assert str2bool(False) is False
    assert str2bool('false') is False
    assert str2bool('FALSE') is False
    assert str2bool('0') is False
    assert str2bool('no') is False
    assert str2bool('n') is False
    try:
        str2bool('hana')
    except argparse.ArgumentTypeError:
        pass

def test_shell_command():
    run_shell_command('ls')

def test_shell_command_with_output():
    run_shell_command(command='ls', print_output=True)

def test_shell_command_with_raise():
    try:
        run_shell_command(command='this is not a command', raise_output=True)
    except ShellCommandException:
        pass
