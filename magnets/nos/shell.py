#! usr/bin/python
# -*- coding: iso-8859-15 -*-

""" nos shell \n
The Nocturnal OS command prompt
"""


def get_command():
    # type: () -> object
    """
    Prints a command prompt and returns the command entered
    :return:
    """
    command = raw_input("nos:$> ")
    assert isinstance(command, object)
    return command


def echo_command(i):
    # type: (object) -> object
    """
    Just echoes the command input from the shell module
    :param i:
    """
    print i
