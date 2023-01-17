#!/usr/bin/python3
def uppercase(str):
    n = 0
    for i in range(0, len(str)):
        if 96 < ord(str[i]) < 123:
            n = 32
        else:
            n = 0
        print(chr((ord(str[i]) - n)).format(), end="")
    print("")
