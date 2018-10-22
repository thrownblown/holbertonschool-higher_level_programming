#!/usr/bin/python3
""" Base class unittest """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.r0 = Base()
        self.r1 = Base(id=33)

    def test_id(self):
        self.assertEqual(self.r0.id, 1)
        self.assertEqual(self.r1.id, 33)
