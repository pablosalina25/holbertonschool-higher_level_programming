#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:{}".format(sys.argv[1]))
    elif len(sys.argv) > 2:
        print("{} arguments: {}".format(len(sys.argv), sys.argv[1:]))
