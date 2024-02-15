#!/usr/bin/python3
"""
Test cases for the Square class.
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Test cases for the Square class
    """

    def test_constructor(self):
        """
        Test initialization.
        """
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_init_with_negative_values(self):
        """
        Test initialization with negative size value.
        """
        with self.assertRaises(ValueError) as exc:
            Square(-5)
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_init_with_zero_value(self):
        """
        Test initialization with zero size value.
        """
        with self.assertRaises(ValueError) as exc:
            Square(0)
        self.assertEqual(str(exc.exception), "width must be > 0")

    def test_init_with_empty_value(self):
        """
        Test initialization with empty value.
        """
        with self.assertRaises(TypeError):
            Square()

    def test_init_with_none_value(self):
        """
        Test initialization with None value.
        """
        with self.assertRaises(TypeError) as exc:
            Square(None)
        self.assertEqual(str(exc.exception), "width must be an integer")

    def test_size_property(self):
        """
        Test the size property.
        """
        square = Square(3)
        self.assertEqual(square.size, 3)

    def test_size_setter(self):
        """
        Test the size setter.
        """
        square = Square(3)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_update_with_positional_args(self):
        """
        Test update method with positional arguments.
        """
        square = Square(3)
        square.update(4, 5, 6, 7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_update_with_keyword_args(self):
        """
        Test update method with keyword arguments.
        """
        square = Square(3)
        square.update(id=4, size=5, x=6, y=7)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 7)

    def test_to_dictionary(self):
        """
        Test to_dictionary method.
        """
        square = Square(3, 4, 5, 6)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {'id': 6, 'side_length': 3, 'x': 4, 'y': 5})

    def test_str_representation(self):
        """
        Test string representation.
        """
        square = Square(3, 4, 5, 6)
	self.assertEqual(str(square), "[Square] (6) 4/5 - 3")
