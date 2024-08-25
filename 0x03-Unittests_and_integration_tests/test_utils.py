#!/usr/bin/env python3
'''test the function'''

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''the class testing the function utils'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Test case 1
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Test case 2
        ({"a": {"b": 2}}, ("a", "b"), 2),  # Test case 3
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''the methods access'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''using the raise to handle th error'''
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check if the exception message is as expected
        self.assertEqual(str(context.exception), repr(path[-1]))


if __name__ == '__main__':
    unittest.main()
