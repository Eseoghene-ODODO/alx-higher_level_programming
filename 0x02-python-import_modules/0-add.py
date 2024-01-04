#!/usr/bin/python3
from add_0 import add
if __name__ == '__main__':
    """
        Python script that imports a function called add from add_0
        Arguments:
            a = 1
            b = 2
            print('{} + {} = {}'. format(a, b, add(a, b))
        final result becomes 1 + 2 = 3
    """
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
