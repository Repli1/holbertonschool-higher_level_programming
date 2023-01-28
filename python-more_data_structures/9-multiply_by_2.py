#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    if len(a_dictionary) == 0:
        return b_dictionary
    for key in b_dictionary:
        b_dictionary[key] *= 2
    return b_dictionary
