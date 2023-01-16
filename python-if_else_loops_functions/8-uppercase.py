#!/usr/bin/python3
def uppercase(str):
    n = 0
    for i in range(0, len(str)):
        if 96 < ord(str[i]) < 123:
            n = 32
        else:
            n = 0
        if i == (len(str) - 1):
            print(chr((ord(str[i]) - n)).format())
        else:
            print(chr((ord(str[i]) - n)).format(), end="")
