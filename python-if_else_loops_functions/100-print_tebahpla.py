#!/usr/bin/env python3
for i in range(122, 96, -1):
    # If the distance from 'z' is odd, make it uppercase
    if (122 - i) % 2 != 0:
        print("{}".format(chr(i - 32)), end="")
    else:
        print("{}".format(chr(i)), end="")
