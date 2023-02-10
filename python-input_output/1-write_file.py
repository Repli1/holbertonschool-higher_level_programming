#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes a file, if name exists, replaces file"""
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
