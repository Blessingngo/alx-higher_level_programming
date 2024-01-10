#!/usr/bin/python3
"""
Read from a file and prints
"""


def read_file(filename=""):
    """
    Reads from filename and prints
    its contents to stdout.
    Args:
     - filename: name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")