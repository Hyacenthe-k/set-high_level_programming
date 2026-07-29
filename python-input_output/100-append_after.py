#!/usr/bin/python3
"""Module inserting a line of text after matching strings in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a string after each line containing a specific search string."""
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
