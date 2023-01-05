#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]

    arguments = [int(args) for args in arguments]

    result = sum(arguments)
    print(result)
