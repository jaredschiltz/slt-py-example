"""
Author: Jared Schiltz
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""
from math import pi
from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.right_triangle = Triangle(3, 4, pi/2)
        self.right_and_isosceles_triangle = Triangle(4, 4, pi/2)
        self.not_right_or_isosceles_triangle = Triangle(3, 4, pi/7)
        self.isosceles_triangle = Triangle(2, 2, 60 * pi / 180)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertAlmostEqual(self.right_triangle.area(), 6)
        self.assertAlmostEqual(self.right_and_isosceles_triangle.area(), 8.01)
        self.assertAlmostEqual(self.not_right_or_isosceles_triangle.area(), 2.61)
        self.assertAlmostEqual(self.isosceles_triangle.area(), 1.73)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertAlmostEqual(self.right_triangle.perimeter(), 12)
        self.assertAlmostEqual(self.right_and_isosceles_triangle.perimeter(), 13.66)
        self.assertAlmostEqual(self.not_right_or_isosceles_triangle.perimeter(), 8.84)
        self.assertAlmostEqual(self.isosceles_triangle.perimeter(), 6.0)

    def test_is_right_triangle(self):
        """
        Determine if triangle is a right triangle
        """ 
        self.assertEqual(self.right_triangle.is_right_triangle(), True)
        self.assertEqual(self.right_and_isosceles_triangle.is_right_triangle(), True)
        self.assertEqual(self.not_right_or_isosceles_triangle.is_right_triangle(), False)
        self.assertEqual(self.isosceles_triangle.is_right_triangle(), False)

    def test_is_isosceles_triangle(self):
        """
        Determine if triangle is an isosceles triangle
        """ 
        self.assertEqual(self.right_triangle.is_isosceles_triangle(), False)
        self.assertEqual(self.right_and_isosceles_triangle.is_isosceles_triangle(), True)
        self.assertEqual(self.not_right_or_isosceles_triangle.is_isosceles_triangle(), False)
        self.assertEqual(self.isosceles_triangle.is_isosceles_triangle(), True)