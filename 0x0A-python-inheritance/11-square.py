#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents the sub class Square."""

    def __init__(self, size):
        """Initialize an instance of the class Square."""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
