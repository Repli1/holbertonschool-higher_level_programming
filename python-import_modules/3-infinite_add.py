#!/usr/bin/python3
import sys
n = 0
if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        n += int(sys.argv[i])
    print(n)
