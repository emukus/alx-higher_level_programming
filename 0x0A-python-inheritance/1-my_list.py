#!/usr/bin/python3
"""Defines class MyList inherited from list."""


class MyList(list):
    """Implements sorted printing for buit-in list class."""

    def print_sorted(self):
        """Prints list sorted in ascending order."""
        print(sorted(self))
