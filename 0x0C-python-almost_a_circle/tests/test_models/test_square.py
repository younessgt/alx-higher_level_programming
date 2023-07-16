#!/usr/bin/python3
""" testing the module rectangle """
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
        self.assertEqual(r1.id, 1)

        r2 = Square(10, 1, 7)
        self.assertTrue(r2.width == 10)
        self.assertTrue(r2.height == 10)
        self.assertTrue(r2.x == 1)
        self.assertTrue(r2.y == 7)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 3, 0)
        self.assertTrue(r3.width == 10)
        self.assertTrue(r3.height == 2)
        self.assertTrue(r3.x == 3)
        self.assertTrue(r3.y == 0)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(1, 2, 0, 0, 11)
        self.assertTrue(r4.width == 1)
        self.assertTrue(r4.height == 2)
        self.assertTrue(r4.x == 0)
        self.assertTrue(r4.y == 0)
        self.assertEqual(r4.id, 11)

        r5 = Rectangle(13, 1)
        self.assertEqual(r5.id, 5)

    def test_case_area(self):
        """ test cases for area module """
        a = Rectangle(5, 10)
        self.assertEqual(a.area(), 50)

        b = Rectangle(10, 10)
        self.assertEqual(b.area(), 100)

    def test_type_value(self):

        """ Testing different case concerning types and value
        for [width, height x, y]
        - Testing cases -> [int, float, float('nan'), float('inf'),
        string, list, tuple, dict, empty, None]"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("a", 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([1, 3], 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(float('nan'), 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("float(inf)", 12)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 12)

        with self.assertRaises(TypeError):
            r = Rectangle()

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "a")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, float('nan'))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, float('inf'))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [12, 10])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (1, 5))

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(10, -1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 12, "a")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 12, [1, 10, 19])

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 12, -2)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 12, 1, "a")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(10, 12, 1, {"key": "hello"})

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 12, 10, -4)

    def test_dispaly(self):
        """ test case for display method
        - test case without x and y
        - test case using x and y """
        expected = ("###\n###\n")
        capt_stdout = StringIO()
        sys.stdout = capt_stdout
        a = Rectangle(3, 2)
        a.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capt_stdout.getvalue(), expected)

        expected_2 = ("##\n##\n")
        capt2_stdout = StringIO()
        with redirect_stdout(capt2_stdout):
            b = Rectangle(2, 2)
            b.display()
        self.assertEqual(capt2_stdout.getvalue(), expected_2)

        expected_3 = ("\n\n  ##\n  ##\n")
        capt3_stdout = StringIO()
        with redirect_stdout(capt3_stdout):
            b = Rectangle(2, 2, 2, 2)
            b.display()
        self.assertEqual(capt3_stdout.getvalue(), expected_3)

        expected_4 = (" ###\n ###\n")
        capt4_stdout = StringIO()
        with redirect_stdout(capt4_stdout):
            b = Rectangle(3, 2, 1, 0)
            b.display()
        self.assertEqual(capt4_stdout.getvalue(), expected_4)

    def test_string(self):
        """ test case for __str__ magic method"""
        k = Rectangle(10, 10, 0, 0, 15)
        self.assertEqual(str(k), "[Rectangle] (15) 0/0 - 10/10")

    def test_update(self):
        """ test case for update method
        - test case for args
        - test case for kwargs"""
        la = Rectangle(10, 10, 10, 10, 1)
        la.update()
        self.assertEqual(str(la), "[Rectangle] (1) 10/10 - 10/10")

        la.update(8)
        self.assertEqual(str(la), "[Rectangle] (8) 10/10 - 10/10")

        la.update(12, 3)
        self.assertEqual(str(la), "[Rectangle] (12) 10/10 - 3/10")

        la.update(12, 3, 7)
        self.assertEqual(str(la), "[Rectangle] (12) 10/10 - 3/7")

        la.update(12, 3, 7, 10, 2)
        self.assertEqual(str(la), "[Rectangle] (12) 10/2 - 3/7")

        la.update(12, 3, 7, 10, 2, 17)
        self.assertEqual(str(la), "[Rectangle] (12) 10/17 - 3/7")

        la.update(12, 3, 7, 10, 2, 17, width=100)
        self.assertEqual(str(la), "[Rectangle] (12) 10/17 - 3/7")

        la.update(12, width=100)
        self.assertEqual(str(la), "[Rectangle] (12) 10/17 - 3/7")

        la.update(width=100)
        self.assertEqual(str(la), "[Rectangle] (12) 10/17 - 100/7")

        la.update(id=11, width=100, x=5)
        self.assertEqual(str(la), "[Rectangle] (11) 5/17 - 100/7")

    def test_to_dict(self):
        """ test cases for to_dictionary method """

        r1 = Rectangle(10, 2, 1, 9)
        with self.assertRaises(
                TypeError,
                msg="to_dictionary() takes 1\
                        positional argument but 2 were given"):
            r1_dictionary = r1.to_dictionary(12)
        r1_dictionary = r1.to_dictionary()
        self.assertTrue(type(r1_dictionary) == dict)
        self.assertTrue(
                r1_dictionary ==
                {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(15, 7, 0, 0, 18)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")


if __name__ == "__main__":
    unittest.main()
