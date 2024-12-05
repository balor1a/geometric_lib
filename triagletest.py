import unittest

from triagle import *

class RectangleTestCase(unittest.TestCase) :
    def test_perimeter_null_a(self):
       res = perimeter(0, 10, 3)
       self.assertEqual(res,0)
    def test_perimeter_null_b(self):
       res = perimeter(12, 0, 5)
       self.assertEqual(res,0)
    def test_perimeter_fractional(self):
       res = perimeter(2.3, 4.78, 5)
       self.assertEqual(res, 14.16)
    def test_perimeter_negative(self):
       res = perimeter(-23, -34)
       self.assertEqual(res, 0)
    def test_area_null_a(self):
       res = area(435, 0)
       self.assertEqual(res,0)
    def test_area_null_b(self):
       res = area(0, 321)
       self.assertEqual(res,0)
    def test_area_negative(self):
       res = area(-14, 3)
       self.assertEqual(res, 0)
    def test_area_fractional(self):
       res = area(3.7, 2)
       self.assertEqual(res, 3,7)