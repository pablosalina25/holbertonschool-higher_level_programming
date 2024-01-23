#!/usr/bin/python3
for alp in range(97, 123):
    if alp == 101 or alp == 113:
        alp += 1
    print("{}".format(chr(alp)), end="")
