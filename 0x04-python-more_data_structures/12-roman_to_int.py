#!/usr/bin/python3
"""
A function that converts roman numerals to integers
"""


def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
            'I': 1, 'V': 5,
            'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    result = 0

    for i in range(len(roman_string)):
        current_value = roman_numerals[roman_string[i]]
        next_value = roman_numerals[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

        if current_value < next_value:
            result += (next_value - current_value)
            i += 1  # Skip the next character

        else:
            result += current_value

    return result
