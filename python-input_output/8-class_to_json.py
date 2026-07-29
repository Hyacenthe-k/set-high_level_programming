#!/usr/bin/python3
"""Module returning dictionary description for JSON serialization of object."""


def class_to_json(obj):
    """Returns dictionary description with simple data structure for JSON."""
    return obj.__dict__
