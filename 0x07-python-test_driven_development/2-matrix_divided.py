#!/usr/bun/python3
"""Define a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
        for row in matrix:
            if type(row) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
                if size is None:
                    size = len(row)
                elif size != len(row):
                    raise TypeError("Each row of the matrix must have the same size")
                for i in row:
                    if type(i) is not int and type(i) is not float:
                        raise TypeError("matrix must be a matrix(list of lists) of \
                                integers/floats")
    if type(div) is not int  and type(div) is not float:
        raise TypeError("div must be a number")
    if div < 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
