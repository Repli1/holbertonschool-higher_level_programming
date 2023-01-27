#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        return 0
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
