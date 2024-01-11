#!/usr/bin/python3
"""
A function that converts a roman numeral to an integer
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  number = 0
  i = 0

  while i < len(roman_string):
      first_char = roman_numerals[roman_string[i]]
    if i + 1 < len(roman_string):
        next_char = roman_numerals[roman_string[i + 1]]
      if first_char < next_char:
          number -= first_char
      else:
          number += first_char
    else:
        number += first_char
    i += 1

  return number
