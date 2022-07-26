#!/usr/bin/python3
"""Defines a text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if i == '.' or i == '?' or i == ':':
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
