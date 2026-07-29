#!/usr/bin/python3
"""Module that contains a function that appends a string to a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
