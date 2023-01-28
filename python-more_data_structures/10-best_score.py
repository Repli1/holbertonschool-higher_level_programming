#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    n = 0
    for key in a_dictionary:
        if a_dictionary[key] > n or (n == 0 and a_dictionary[key] > n):
            n = a_dictionary[key]
    for key in a_dictionary:
        if a_dictionary[key] == n:
            return key
