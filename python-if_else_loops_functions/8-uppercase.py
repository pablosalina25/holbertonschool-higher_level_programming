#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        ch = ord(ch)
        if ch > 96 and ch < 123:
            ch -= 32
        print("{}".format(chr(ch)), end="")
    print()
