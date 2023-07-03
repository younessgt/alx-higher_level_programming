#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    this class is for testing the max_integer function
    """

    def test_positive(self):
        """testing positive numbers, int and float"""
        self.assertEqual(max_integer([1, 5, 6]), 6)
        self.assertEqual(max_integer([10.5, 1, 7]), 10.5)
        self.assertEqual(max_integer([100]), 100)

    def test_negative(self):
        """testing negative and positive numbers"""
        self.assertEqual(max_integer([-11, -5, -17]), -5)
        self.assertEqual(max_integer([0, -12, -3]), 0)
        self.assertEqual(max_integer([-100]), -100)

    def test_type(self):
        """ testing different data types """
        self.assertEqual(max_integer((1, 10, 7, 3)), 10)
        self.assertEqual(max_integer("hello"), "o")
        self.assertEqual(max_integer(["hello", "world"]), "world")
    def test_empty(self):
        """ testing different empty cases"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
