#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Representation of class Student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of Student instance."""
        return self.__dict__
