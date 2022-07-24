from unittest import TestCase
from robust_area_of_triangle import area_of_triangle


class TestAreaOfTriangle(TestCase):

    def test_float_values(self):
        """ Test areas when values are floats """
        self.assertAlmostEqual(area_of_triangle(3.4556, 8.3567), 14.43870626)
        self.assertEqual(area_of_triangle(2.3, 5.7), 6.555)

    def test_integer_values(self):
        """ Test areas when values are integers """
        self.assertEqual(area_of_triangle(2, 5), 5.0)
        self.assertEqual(area_of_triangle(4, 6), 12.0)

    def test_zero_base(self):
        """ Test areas when base is zero """
        self.assertEqual(area_of_triangle(0, 5), 0.0)

    def test_zero_height(self):
        """ Test areas when height is zero """
        self.assertEqual(area_of_triangle(5, 0), 0.0)

    def test_zero_values(self):
        """ Test areas when base and height are zero """
        self.assertEqual(area_of_triangle(0, 0), 0.0)
 
    def test_with_boolean(self):
        """ Test that TypeError is raised with boolean types """
        self.assertRaises(TypeError, area_of_triangle, True, 5)
        self.assertRaises(TypeError, area_of_triangle, 2, True)

    def test_with_string(self):
        """ Test that TypeError is raised with string types """
        self.assertRaises(TypeError, area_of_triangle, "base", 5)
        self.assertRaises(TypeError, area_of_triangle, 2, "height")

    def test_with_nulls(self):
        """ Test that TypeError is raised with null types """
        self.assertRaises(TypeError, area_of_triangle, None, 5)
        self.assertRaises(TypeError, area_of_triangle, 2, None)

    def test_non_negative_base(self):
        """ Testing the valueError is raised with negative base """
        self.assertRaises(ValueError, area_of_triangle, -2, 5)

    def test_non_negative_height(self):
        """ Testing the valueError is raised with negative height """
        self.assertRaises(ValueError, area_of_triangle, 5, -2)
       
    def test_non_negative_values(self):
        """ Testing the non negative base and height """
        self.assertRaises(ValueError, area_of_triangle, -2, -5)
