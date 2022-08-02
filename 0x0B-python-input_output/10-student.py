#!/usr/bin/python3
"""Define a class Student"""


class Student:
    """Representation of class Student."""

    def __init__(self, first_name, last_name, age):
        """Initialises a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            retrieves a dictionary representation of Student.
            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
