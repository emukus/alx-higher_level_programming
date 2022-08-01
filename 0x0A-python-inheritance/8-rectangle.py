#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a class Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.
        Args:
            width (int): width of the new rectangle
            height (int): height of the new rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
