import unittest

from circle import *

class RectangleTestCase(unittest.TestCase) :
    def test_perimeter_null_a(self):
       res = perimeter(5)
       self.assertEqual(res, 31.4159265359)
    def test_perimeter_null_b(self):
       res = perimeter(0)
       self.assertEqual(res,0)
    def test_perimeter_negative(self):
       res = perimeter(-23)
       self.assertEqual(res, 0)
    def test_area_null_a(self):
       res = area(0)
       self.assertEqual(res,0)
    def test_area_null_b(self):
       res = area(5)
       self.assertEqual(res,78.5398163397)
    def test_area_negative(self):
       res = area(-12)
       self.assertEqual(res, 0)
    