#!/usr/bin/python3
""" Unittest for rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r0 = Rectangle(2, 1)
        self.r1 = Rectangle(5, 4)
        self.r2 = Rectangle(1, 1, 1, 1, 32)
        self.r3 = Rectangle(3, 6, 0, 0, 13)
        self.r4 = Rectangle(1, 1, 1, 1, 64)
        self.r5 = Rectangle(1, 2, 5, 6, 5)
        self.r6 = Rectangle(3, 3, 3, 3, 256)
        self.r7 = Rectangle(2, 2, 2, 2, 128)

    def test_id(self):
        self.assertEqual(self.r0.id, 6)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r2.id, 32)
        self.assertEqual(self.r3.id, 13)

    def test_str(self):
        self.assertEqual(str(self.r0), "[Rectangle] (8) 0/0 - 2/1")
        self.assertEqual(str(self.r1), "[Rectangle] (9) 0/0 - 5/4")
        self.assertEqual(str(self.r2), "[Rectangle] (32) 1/1 - 1/1")
        self.assertEqual(str(self.r3), "[Rectangle] (13) 0/0 - 3/6")

    def test_update(self):
        self.r4.update(89)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 1/1 - 1/1")
        self.r4.update(89, 2)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 1/1 - 2/1")
        self.r4.update(89, 2, 3)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 1/1 - 2/3")
        self.r4.update(89, 2, 3, 4)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 4/1 - 2/3")
        self.r4.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 4/5 - 2/3")
        self.r4.update(1, 1, 1, 1, 1)
        self.r4.update(height=2)
        self.assertEqual(str(self.r4), "[Rectangle] (1) 1/1 - 1/2")
        self.r4.update(width=2, x=2)
        self.assertEqual(str(self.r4), "[Rectangle] (1) 2/1 - 2/2")
        self.r4.update(x=3, height=3, y=3, width=3, id=89)
        self.assertEqual(str(self.r4), "[Rectangle] (89) 3/3 - 3/3")

    def test_area(self):
        self.assertEqual(self.r0.area(), 2)
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 1)
        self.assertEqual(self.r3.area(), 18)

    def test_width(self):
        self.assertEqual(self.r0.width, 2)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r3.width, 3)

    def test_height(self):
        self.assertEqual(self.r0.height, 1)
        self.assertEqual(self.r1.height, 4)
        self.assertEqual(self.r2.height, 1)
        self.assertEqual(self.r3.height, 6)

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
        self.assertRaises(TypeError, Rectangle, False, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, None, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, (1, 1), 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, "1", 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, [1, 1], 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, {'1': 1}, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1.1, 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, float('nan'), 1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, float('inf'), 1, 1, 1, 1)

    def test_height_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, False, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, None, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, "1", 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, {'1': 1}, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, [1, 1], 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, (1, 1), 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1.1, 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, float('inf'), 1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, float('nan'), 1, 1, 1)

    def test_x_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, False, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, None, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, "1", 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, {'1': 1}, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, [1, 1], 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, (1, 1), 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1.1, 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, float('nan'), 1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, float('inf'), 1, 1)

    def test_y_Type_error(self):
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, False, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, None, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, {'1': 1}, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, "1", 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, (1, 1), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, [1, 1], 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, 1.1, 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, float('nan'), 1)
        self.assertRaises(TypeError, Rectangle, 1, 1, 1, float('inf'), 1)

    def test_width_Value_error(self):
        self.assertRaises(ValueError, Rectangle, -1, 1, 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, 0, 1, 1, 1, 1)

    def test_height_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, 0, 1, 1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -1, 1, 1, 1)

    def test_y_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, 1, -1, 1)

    def test_x_Value_error(self):
        self.assertRaises(ValueError, Rectangle, 1, 1, -1, 1, 1)
