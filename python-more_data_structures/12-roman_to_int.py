#!/usr/bin/python3
def roman_to_int(roman_string):
    translate = {"I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    n = 0
    for i in range(0, len(roman_string)):
        if i != len(roman_string) - 1:
            if translate[roman_string[i]] < translate[roman_string[i + 1]]:
                n -= translate[roman_string[i]]
            else:
                n += translate[roman_string[i]]
        else:
            n += translate[roman_string[i]]
    return n
