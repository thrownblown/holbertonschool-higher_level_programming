#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(max_integer("abcdefghiaaaaa"), 'i')
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(['a', 'b', 'z']), 'z')
        self.assertEqual(max_integer(['a', 'A']), 'a')
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 5, -5]), 5)
        self.assertEqual(max_integer([1, 5, -6]), 5)
        self.assertEqual(max_integer([1, 6, 8, 3]), 8)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

if __name__ == __main__:
    unittest.main()
