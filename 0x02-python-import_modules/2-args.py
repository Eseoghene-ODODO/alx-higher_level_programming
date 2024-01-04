#!/usr/bin/python3
from sys import argv
for i in range(len(argv)):
    if len(argv) == 1:
        print("{} argument:\n{}: {}".format(len(argv) - 1, i + 1, argv))
    elif len(argv) > 1:
        print("{} arguments:\n{}: {}".format(len(argv) - 1, i + 1, argv))
    else:
        print("{} arguments.".format(i))
