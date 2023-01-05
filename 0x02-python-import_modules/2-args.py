#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = 1
    if (len(sys.argv) < 2):
        print("0 arguments.")
    elif (len(sys.argv) < 3):
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for arg in sys.argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i += 1
