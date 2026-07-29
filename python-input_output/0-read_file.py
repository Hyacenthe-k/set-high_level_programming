#!/usr/bin/python3
"""Module that contains a function that reads a text file and prints it."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
