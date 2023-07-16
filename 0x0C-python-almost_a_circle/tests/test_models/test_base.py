""" tests for the base module """

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json


class TestBase(unittest.TestCase):
    """ class is created """

    def test_int(self):
        """ testing int id """
        a = Base(10)
        self.assertEqual(a.id, 10)

        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_None(self):
        """ testing id = None """

        b = Base()
        self.assertEqual(b.id, 1)
        c = Base()
        self.assertEqual(c.id, 2)
        d = Base()
        self.assertEqual(d.id, 3)

    def test_more_arg(self):
        """ testing Base with more than 1 arg"""
        with self.assertRaises(TypeError):
            a = Base(10, 14)

    def test_json_string(self):
        """ testing the to_json_string static method """

        dictionary = {"x": 1, "y": 4, "id": 1, "height": 3, "width": 5}
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(
                json_dict,
                '[{"x": 1, "y": 4, "id": 1, "height": 3, "width": 5}]')
        self.assertTrue(type(json_dict) == str)

        r2 = Rectangle(1, 2, 3, 4, 12)
        dictionary = r2.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(
                json_dict,
                '[{"x": 3, "y": 4, "id": 12, "height": 2, "width": 1}]')
        self.assertTrue(type(json_dict) == str)

        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, '[]')
        self.assertTrue(type(json_dict) == str)

        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, '[]')
        self.assertTrue(type(json_dict) == str)

        json_dict = Base.to_json_string([{}])
        self.assertEqual(json_dict, '[{}]')

    def test_save_tofile(self):
        """ test case for save_to_file method"""

        r1 = Rectangle(1, 2, 3, 4, 12)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        """ ----------------------------------- --------------------------"""

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1, 2])

        """ ----------------------------------- --------------------------"""

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(["alx", "w"])

        """ ----------------------------------- --------------------------"""

        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as rf:
            self.assertEqual(
                    rf.read(), Base.to_json_string([r1.to_dictionary()]))

        """ ----------------------------------- --------------------------"""

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as rf:
            self.assertEqual(
                    rf.read(),
                    '[]')
        """ ----------------------------------- --------------------------"""

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as rf:
            self.assertEqual(
                    rf.read(),
                    '[]')

    def test_from_json(self):
        """ test cases for from_json_string static method """

        list_di_str = '[{"name": "json", "School": "alx", "graduated": true}]'
        list_di = [{"name": "json", "School": "alx", "graduated": True}]
        with self.assertRaises(TypeError):
            res = Base.from_json_string(list_di)
        
        """ ----------------------------------- --------------------------"""
        
        list_di_str = '[{"name": "json", "School": "alx", "graduated": true}]'
        list_di = [{"name": "json", "School": "alx", "graduated": True}]
        res = Base.from_json_string(list_di_str)
        self.assertEqual(res, list_di)
        self.assertTrue(type(res) == list)
        self.assertTrue(type(res[0]) == dict)
    
        """ ----------------------------------- --------------------------"""
        list_di_str = '[]'
        list_di = []
        res = Base.from_json_string(list_di_str)
        self.assertEqual(res, list_di)
        self.assertTrue(type(res) == list)

        """ ----------------------------------- --------------------------"""

        list_di_str = None
        list_di = []
        res = Base.from_json_string(list_di_str)
        self.assertEqual(res, list_di)
        self.assertTrue(type(res) == list)

        """ ----------------------------------- --------------------------"""

        with self.assertRaises(TypeError):
            res = Base.from_json_string()

        """ ----------------------------------- --------------------------"""

        list_di_str = ''
        list_di = []
        res = Base.from_json_string(list_di_str)
        self.assertEqual(res, list_di)

    def test_create_in(self):
        """ test cases for create class method """

        r = Square(10, 1, 2, 5)
        r_di = {"size": 10, "x": 1, "y": 2, "id": 5}
        new = Square.create(**r_di)
        self.assertEqual(str(r), str(new))
        self.assertFalse(r == new)

        """ ----------------------------------- --------------------------"""

        r1 = Rectangle(7, 2, 1)
        r1_di = r1.to_dictionary()
        r2 = Rectangle.create(**r1_di)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_load_from_file(self):
        """ test cases for load_from_file method
        """

        """ testing for None file """

        Rectangle.save_to_file(None)

        list_re= Rectangle.load_from_file()
        self.assertEqual(type(list_re), list)
        self.assertEqual(list_re, [])

        """ ----------------------------------- --------------------------"""

        """ testing empty list"""
        Rectangle.save_to_file([])

        list_re= Rectangle.load_from_file()
        self.assertEqual(type(list_re), list)
        self.assertEqual(list_re, [])        

        """ ----------------------------------- --------------------------"""

        """ testing list of 2 instances """
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(6, 7, 8, 9, 10)

        Rectangle.save_to_file([a, b])

        list_re= Rectangle.load_from_file()
        self.assertEqual(type(list_re), list)

        for idx, rect in enumerate(list_re):
            if idx == 0:
                self.assertEqual(str(a), str(rect))
                self.assertFalse(id(a) == id(rect))
            if idx == 1:
                self.assertEqual(str(b), str(rect))
                self.assertFalse(id(b) == id(rect))
