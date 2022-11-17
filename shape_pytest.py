#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""
from math import pi
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import Triangle


def test_rectangle():
    """
    Defines tests on some specific rectangle objects.
    """
    len7wid3 = Rectangle(7, 3)
    len1wid6 = Rectangle(1, 6)
    len5wid5 = Rectangle(5, 5)

    # Test areas, perimeters, and whether they are squares
    assert len7wid3.area() == 21
    assert len1wid6.area() == 6
    assert len5wid5.area() == 25
    assert len7wid3.perimeter() == 20
    assert len1wid6.perimeter() == 14
    assert len5wid5.perimeter() == 20
    assert not len7wid3.is_square()
    assert not len1wid6.is_square()
    assert len5wid5.is_square()


def test_circle():
    """
    Defines tests on some specific circle objects.
    """
    radius5 = Circle(5)
    radius8 = Circle(8)

    # Test areas, perimeters, and diameters
    assert radius5.area() == 78.54
    assert radius8.area() == 201.06
    assert radius5.perimeter() == 31.42
    assert radius8.perimeter() == 50.27
    assert radius5.diameter() == 10
    assert radius8.diameter() == 16

def test_triangle():
    """
    Defines tests on some specific triangle objects.
    """
    right_triangle = Triangle(3, 4, pi/2)
    right_and_isosceles_triangle = Triangle(4, 4, pi/2)
    not_right_or_isosceles_triangle = Triangle(3, 4, pi/7)
    isosceles_triangle = Triangle(2, 2, 60 * pi / 180)
    
    # Test areas, perimeters, and triangle type checks
    assert right_triangle.area() == 6
    assert right_and_isosceles_triangle.area() == 8.01
    assert not_right_or_isosceles_triangle.area() == 2.61
    assert isosceles_triangle.area() == 1.73

    assert right_triangle.perimeter() == 12
    assert right_and_isosceles_triangle.perimeter() == 13.66
    assert not_right_or_isosceles_triangle.perimeter() == 8.84
    assert isosceles_triangle.perimeter() == 6.0

    assert right_triangle.is_right_triangle() 
    assert right_and_isosceles_triangle.is_right_triangle()
    assert not not_right_or_isosceles_triangle.is_right_triangle()
    assert not isosceles_triangle.is_right_triangle()

    assert not right_triangle.is_isosceles_triangle()
    assert right_and_isosceles_triangle.is_isosceles_triangle()
    assert not not_right_or_isosceles_triangle.is_isosceles_triangle()
    assert isosceles_triangle.is_isosceles_triangle()