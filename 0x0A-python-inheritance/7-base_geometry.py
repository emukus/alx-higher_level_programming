#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry():
    """Represents class BaseGeometry."""

    def area(self):
        """Not yet implemented exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a parameter as an integer.
        Args:
            name (str): name of parameter
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an int.
            ValueError: if value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
