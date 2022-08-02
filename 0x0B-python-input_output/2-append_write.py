#!/usr/bin/python3
"""Defines a text-appending function."""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the no. of characters"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
