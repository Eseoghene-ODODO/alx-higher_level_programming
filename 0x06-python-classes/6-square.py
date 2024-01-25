#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """ class body """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize private size and position attributes"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for retrieving private size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for validating and updating private size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for retrieving private position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for validating and updating private position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using #'s"""

        if self.__size == 0:
            # Handle case of 0 size
            print()
            return
        # Print new lines based on position[1]
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            # Print spaces based on position[0]
            print(" " * self.__position[0], end="")
            # Print # based on size
            print("#" * self.__size)
