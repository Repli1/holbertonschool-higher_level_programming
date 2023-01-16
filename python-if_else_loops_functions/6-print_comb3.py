#!/usr/bin/python3
for i in range(0, 100):
    if i % 10 > i//10:
        if i == 89:
            print("{}{}".format(i//10, i % 10))
        else:
            print("{}{}".format(i//10, i % 10), end=", ")
