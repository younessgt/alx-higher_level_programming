#!/usr/bin/python3
""" testing the module square """
from models.square import Square
import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """ class created """
    def test_attr(self):

        """ testing cases for retreiving attributes
        """

        r1 = Square(5)
        self.assertTrue(r1.width == 5)
        self.assertTrue(r1.height == 5)
        self.assertTrue(r1.x == 0)
        self.assertTrue(r1.y == 0)

        r2 = Square(10, 1, 7)
        self.assertTrue(r2.width == 10)
        self.assertTrue(r2.height == 10)
        self.assertTrue(r2.x == 1)
        self.assertTrue(r2.y == 7)
        self.assertEqual(r2.id - 1, r1.id)

        r4 = Square(1, 0, 0, 11)
        self.assertTrue(r4.width == 1)
        self.assertTrue(r4.height == 1)
        self.assertTrue(r4.x == 0)
        self.assertTrue(r4.y == 0)
        self.assertEqual(r4.id, 11)

        r5 = Square(13, 1)
        self.assertEqual(r5.id - 1, r2.id)

    def test_case_area(self):
        """ test cases for area module """
        a = Square(5)
        self.assertEqual(a.area(), 25)

        b = Square(10)
        self.assertEqual(b.area(), 100)

    def test_type_value(self):

        """ Testing different case concerning types and value
        for [width, height x, y]
        - Testing cases -> [int, float, float('nan'), float('inf'),
        string, list, tuple, dict, empty, None]"""

        k = Square(10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            k.size = "a"

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("a", 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square([1, 3], 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(float('nan'), 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("float(inf)", 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(None, 12)

        with self.assertRaises(TypeError):
            r = Square()

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, "a")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, [1, 10, 19])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(1, -2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 1, "a")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(10, 1, {"key": "hello"})

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(1, 12, -4)

    def test_dispaly(self):
        """ test case for display method
        - test case without x and y
        - test case using x and y """
        expected = ("###\n###\n###\n")
        capt_stdout = StringIO()
        sys.stdout = capt_stdout
        a = Square(3)
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capt_stdout.getvalue(), expected)

        expected_2 = ("##\n##\n")
        capt2_stdout = StringIO()
        with redirect_stdout(capt2_stdout):
            b = Square(2)
            b.display()
        self.assertEqual(capt2_stdout.getvalue(), expected_2)

        expected_3 = ("\n\n  ##\n  ##\n")
        capt3_stdout = StringIO()
        with redirect_stdout(capt3_stdout):
            b = Square(2, 2, 2)
            b.display()
        self.assertEqual(capt3_stdout.getvalue(), expected_3)

        expected_4 = (" ##\n ##\n")
        capt4_stdout = StringIO()
        with redirect_stdout(capt4_stdout):
            b = Square(2, 1, 0)
            b.display()
        self.assertEqual(capt4_stdout.getvalue(), expected_4)

    def test_string(self):
        """ test case for __str__ magic method"""
        k = Square(10, 0, 0, 15)
        self.assertEqual(str(k), "[Square] (15) 0/0 - 10")

    def test_update(self):
        """ test case for update method
        - test case for args
        - test case for kwargs"""
        la = Square(10, 10, 10, 1)
        la.update()
        self.assertEqual(str(la), "[Square] (1) 10/10 - 10")

        la.update(8)
        self.assertEqual(str(la), "[Square] (8) 10/10 - 10")

        la.update(12, 3)
        self.assertEqual(str(la), "[Square] (12) 10/10 - 3")

        la.update(12, 3, 7)
        self.assertEqual(str(la), "[Square] (12) 7/10 - 3")

        la.update(12, 3, 7, 2)
        self.assertEqual(str(la), "[Square] (12) 7/2 - 3")

        la.update(12, 3, 7, 10, 2, 17)
        self.assertEqual(str(la), "[Square] (12) 7/17 - 3")

        la.update(12, 3, 7, 10, 2, 17, size=100)
        self.assertEqual(str(la), "[Square] (12) 7/17 - 3")

        la.update(12, size=100)
        self.assertEqual(str(la), "[Square] (12) 7/17 - 3")

        la.update(size=100)
        self.assertEqual(str(la), "[Square] (12) 7/17 - 100")

        la.update(id=11, size=100, x=5)
        self.assertEqual(str(la), "[Square] (11) 5/17 - 100")

    def test_to_dict(self):
        """ test cases for to_dictionary method """

        r1 = Square(10, 2, 1, 13)
        with self.assertRaises(
                TypeError,
                msg="to_dictionary() takes 1\
                        positional argument but 2 were given"):
            r1_dictionary = r1.to_dictionary(12)

        r1_dictionary = r1.to_dictionary()
        self.assertTrue(type(r1_dictionary) == dict)
        self.assertEqual(
                r1_dictionary,
                {'x': 2, 'y': 1, 'id': 13, 'size': 10})
        r2 = Square(15, 7, 0)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Square] (13) 2/1 - 10")


if __name__ == "__main__":
    unittest.main()
