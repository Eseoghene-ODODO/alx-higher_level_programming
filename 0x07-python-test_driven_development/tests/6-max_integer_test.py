#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    """ test body """
    def test_max_integer_case1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Should return the maximum integer in the list")

    def test_max_integer_case2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4, "Should return the maximum integer in the list")

if __name__ == '__main__':
    unittest.main()
