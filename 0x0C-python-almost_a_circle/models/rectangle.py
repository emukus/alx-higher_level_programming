#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle that inherits from class Base"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initializes a new rectangle."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        The __str__() method returns a string representation of the object
        return: The id, x, y, width, and height of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):
        """Validates all types and values."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """Width getter
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """Width setter
        Sets the width of the rectangle
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """Height getter
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """Height setter
        Sets the height of the rectangle
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """Getter for the private variable __x
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """Setter for the private variable __x
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """Getter for the private variable __x
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """Setter for the private variable __x
        """
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int:
        """Returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints # shape of the rectangle
        """
        print('\n'*self.y, end='')
        for h in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):
        """Updates rectangle attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Rectangle to dictionary
        Returns the dictionary representation of a Rectangle
        return: A dictionary with id, width, height, x, and y of the rectangle
        """

        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
            }
