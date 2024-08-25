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


if __name__ == '__main__':
    unittest.main()
