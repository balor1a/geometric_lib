import unittest

from square import *

class RectangleTestCase(unittest.TestCase) :
    def test_perimeter_null_a(self):
       res = perimeter(6)
       self.assertEqual(res, 24)
    def test_perimeter_null_b(self):
       res = perimeter(0)
       self.assertEqual(res,0)
    def test_perimeter_fractional(self):
       res = perimeter(5.5)
       self.assertEqual(res, 22)
    def test_perimeter_negative(self):
       res = perimeter(-23)
       self.assertEqual(res, 0)
    def test_area_null_a(self):
       res = area(0)
       self.assertEqual(res,0)
    def test_area_null_b(self):
       res = area(12)
       self.assertEqual(res,144)
    def test_area_negative(self):
       res = area(-12)
       self.assertEqual(res, 0)
    def test_area_fractional(self):
       res = area(0.6)
       self.assertEqual(res,0.36)