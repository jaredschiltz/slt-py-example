#!/usr/bin/env python

"""
Author: Jared Schiltz
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from math import pi, sqrt, cos, sin, isclose
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains the lengths and angles of the triangle.
    The number of decimal places is used to specify the precision when computing values.
    """

    decimal_places = 2

    def __init__(self, length_a, length_b, angle_c):
        """
        Create the triangle by taking two length parameters and one angle parameter.
        Calculate the other two angles and the third length. 
        Store all parameters as object members.

        Important Note: Angle parameters to be specified in radians!
        """
        self.length_a = length_a
        self.length_b = length_b
        self.angle_c = angle_c
        self.length_c = self.law_of_cosines(self.length_a, self.length_b, self.angle_c)
        self.angle_a = self.law_of_sines(self.length_c, self.length_a, self.angle_c)
        self.angle_b = self.law_of_sines(self.length_c, self.length_b, self.angle_c)

    def area(self):
        """
        Compute the area using Heron's formula
        """
        return round(self.herons_formula(), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter
        """
        return round(self.length_a + self.length_b + self.length_c, self.decimal_places)

    def is_right_triangle(self):
        """
        Determine if triangle is right triangle.
        Return boolean
        """
        pi_half = pi / 2.0
        return isclose(self.angle_a, pi_half) or isclose(self.angle_b, pi_half) or\
             isclose(self.angle_c, pi_half)

    def is_isosceles_triangle(self):
        """
        Determine if triangle is isosceles triangle.
        Return boolean
        """
        return isclose(self.length_a, self.length_b) or isclose(self.length_b, self.length_c) or\
             isclose(self.length_a, self.length_c)

    def law_of_cosines(self, a, b, c_angle):
        """
        Implement Law Of Cosine function.
        Returns length of side c (across from c_angle) 
        from lengths of a and b and the angle between them
        """
        return sqrt(a ** 2 + b ** 2 - (2 * a * b * cos(c_angle)))

    def law_of_sines(self, a, b, a_angle):
        """
        Implement Law Of Sines function.
        Returns the angle across from side b using the length of a
        and the angle across from side a. 
        """
        return b * sin(a_angle) / a
    
    def herons_formula(self):
        """
        Implement Heron's formula for finding area.
        Returns the area of a triangle in terms of the lengths of all sides
        """
        s = self.perimeter() / 2.0 # This is semi-parameter
        return sqrt(s * (s - self.length_a) * (s - self.length_b) * (s - self.length_c))