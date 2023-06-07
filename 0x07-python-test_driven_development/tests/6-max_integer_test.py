#!/usr/bin/python3
""" Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ TestCase for the max_integer function. """

    def test_regular(self):
        """ Test with a regular list of ints: should return the max result """
        l = [1, 2, 3, 2, 7]
        self.assertEqual(max_integer(l), 7)

    def test_not_int(self):
        """ Test with a list of non-ints and ints:
        should raise a TypeError exception. """
        l = ["i", "b", 8]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """ Test with an empty list: should return None """
        l = []
        self.assertEqual(max_integer(l), None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        l = [-2, -6, 1]
        self.assertEqual(max_integer(l), 1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        l = [3, 7.2, 2]
        self.assertEqual(max_integer(l), 7.2)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 5)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        self.assertEqual(max_integer([8]), 8)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        l = [4, 3, 6, 6, 6]
        self.assertEqual(max_integer(l), 6)

    def test_beginning(self):
        """Test with a list of identical values: should return the value"""
        l = [8, 3, 6, 6, 6]
        self.assertEqual(max_integer(l), 8)
    
    def test_strings(self):
        """Test with a list of strings: should return the second string"""
        l = ["afia", "david"]
        self.assertEqual(max_integer(l), "david")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
