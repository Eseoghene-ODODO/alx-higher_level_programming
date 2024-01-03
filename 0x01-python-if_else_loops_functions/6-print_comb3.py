#!/usr/bin/python3
for numb_1 in range(9):
    for numb_2 in range(numb_1 + 1, 10):
        if numb_1 * 10 + numb_2 < 89:
            print("{:d}{:d}".format(numb_1, numb_2), end=", ")
print("{:d}".format(89))
