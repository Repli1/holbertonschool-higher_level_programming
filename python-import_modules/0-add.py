#!/usr/bin/python3
__import__("0-add")
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}".format())
