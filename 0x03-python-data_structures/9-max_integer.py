#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function that finds the biggest integer of a list."""
    if my_list:
        max = my_list[0]
        for i in my_list:
            if i > max:
                max = i
            return max
        return max
    return None
