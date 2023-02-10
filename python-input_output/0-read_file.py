#!/usr/bin/python3
"""Function read_file"""


def read_file(filename=""):
    """Prints a file to the standard output"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
