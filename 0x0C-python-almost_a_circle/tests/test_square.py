#!/usr/bin/python3
""" Unittest for rectangle class """
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r0 = Square(2)
        self.r1 = Square(5)
        self.r2 = Square(1, 1, 1, 32)
        self.r3 = Square(3, 0, 0, 13)
        self.r4 = Square(1, 1, 1, 64)
        self.r5 = Square(1, 5, 6, 5)
        self.r6 = Square(3, 3, 3, 256)
        self.r7 = Square(2, 2, 2, 128)

    def test_id(self):
        self.assertEqual(self.r0.id, 22)
        self.assertEqual(self.r1.id, 23)
        self.assertEqual(self.r2.id, 32)
        self.assertEqual(self.r3.id, 13)

    def test_str(self):
        self.assertEqual(str(self.r0), "[Square] (24) 0/0 - 2")
        self.assertEqual(str(self.r1), "[Square] (25) 0/0 - 5")
        self.assertEqual(str(self.r2), "[Square] (32) 1/1 - 1")
        self.assertEqual(str(self.r3), "[Square] (13) 0/0 - 3")

    def test_update(self):
        self.r4.update(89)
        self.assertEqual(str(self.r4), "[Square] (89) 1/1 - 1")
        self.r4.update(89, 2)
        self.assertEqual(str(self.r4), "[Square] (89) 1/1 - 2")
        self.r4.update(89, 2, 3)
        self.assertEqual(str(self.r4), "[Square] (89) 3/1 - 2")
        self.r4.update(89, 2, 3, 4)
        self.assertEqual(str(self.r4), "[Square] (89) 3/4 - 2")
        self.r4.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r4), "[Square] (89) 3/4 - 2")
        self.r4.update(1, 1, 1, 1, 1)
        self.r4.update(height=2)
        self.assertEqual(str(self.r4), "[Square] (1) 1/1 - 1")
        self.r4.update(width=2, x=2)
        self.assertEqual(str(self.r4), "[Square] (1) 2/1 - 1")
        self.r4.update(x=3, height=3, y=3, width=3, id=89)
        self.assertEqual(str(self.r4), "[Square] (89) 3/3 - 1")

    def test_area(self):
        self.assertEqual(self.r0.area(), 4)
        self.assertEqual(self.r1.area(), 25)
        self.assertEqual(self.r2.area(), 1)
        self.assertEqual(self.r3.area(), 9)

    def test_width(self):
        self.assertEqual(self.r0.width, 2)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r3.width, 3)

    def test_height(self):
        self.assertEqual(self.r0.width, 2)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r3.width, 3)

    def test_x(self):
        self.assertEqual(self.r0.x, 0)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r5.x, 5)

    def test_y(self):
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r0.y, 0)
        self.assertEqual(self.r6.y, 3)
        self.assertEqual(self.r7.y, 2)


class TestErrorRec(unittest.TestCase):

    def test_width_Type_error(self):
        self.assertRaises(TypeError, Square, False, 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, None, 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, (1, 1), 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, "1", 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, [1, 1], 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, {'1': 1}, 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, 1.1, 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, float('nan'), 1, 1, 1, 1)
        self.assertRaises(TypeError, Square, float('inf'), 1, 1, 1, 1)

    def test_height_Type_error(self):
        self.assertRaises(TypeError, Square, 1, False, 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, None, 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, "1", 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, {'1': 1}, 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, [1, 1], 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, (1, 1), 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, 1.1, 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, float('inf'), 1, 1, 1)
        self.assertRaises(TypeError, Square, 1, float('nan'), 1, 1, 1)

    def test_x_Type_error(self):
        self.assertRaises(TypeError, Square, 1, 1, False, 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, None, 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, "1", 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, {'1': 1}, 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, [1, 1], 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, (1, 1), 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, 1.1, 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, float('nan'), 1, 1)
        self.assertRaises(TypeError, Square, 1, 1, float('inf'), 1, 1)

    def test_y_Type_error(self):
        self.assertRaises(TypeError, Square, 1, 1, 1, False, 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, None, 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, {'1': 1}, 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, "1", 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, (1, 1), 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, [1, 1], 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, 1.1, 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, float('nan'), 1)
        self.assertRaises(TypeError, Square, 1, 1, 1, float('inf'), 1)

    def test_size_Value_error(self):
        self.assertRaises(ValueError, Square, -1, -1, 1, 1)
        self.assertRaises(ValueError, Square, 0, 0, 1, 1)

    def test_y_Value_error(self):
        self.assertRaises(ValueError, Square, 1, 1, -1, 1)

    def test_x_Value_error(self):
        self.assertRaises(ValueError, Square, 1, -1, 1, 1)
