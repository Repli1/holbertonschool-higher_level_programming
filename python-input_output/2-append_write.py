#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """appends string at end of text file and returnes n° of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        append_data = f.write(text)
    return append_data
