#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from HashMap import HashMap
import unittest

"""
Created on Mon Jan  8 18:12:48 2018

@author: tpow
"""

class TestHashMap(unittest.TestCase):
    
    def test_get(self):
        self.assertEqual(new_map.get_value("x"), 3)
        self.assertEqual(new_map.get_value("z"), 9)
        self.assertEqual(new_map.get_value("s"), None)
    
    def test_contains_key(self):
        self.assertTrue(new_map.contains_key("x"))
        self.assertTrue(new_map.contains_key("a"))
        self.assertTrue(new_map.contains_key("b"))
        self.assertTrue(new_map.contains_key("y"))
        self.assertFalse(new_map.contains_key("s"))
    
    def test_contains_value(self):
        self.assertTrue(new_map.contains_value(3))
        self.assertTrue(new_map.contains_value(4))
        self.assertTrue(new_map.contains_value(9))
        self.assertTrue(new_map.contains_value(6))
        self.assertFalse(new_map.contains_value(100))
        
    def test_remove(self):
        new_map.remove("z")
        self.assertFalse(new_map.contains_value(9))
        self.assertFalse(new_map.contains_key("z"))
        self.assertEqual(new_map.get_size(), 4)
        new_map.remove("a")
        new_map.remove("b")
        new_map.remove("y")
        new_map.remove("x")
        self.assertEqual(new_map.get_size(), 0)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestHashMap)
unittest.TextTestRunner(verbosity=2).run(suite)

# for test case above
new_map = HashMap()
new_map.put("x", 3)
new_map.put("y", 4)
new_map.put("z", 5)
new_map.put("z", 6)
new_map.put("z", 9)
new_map.put("b", 7)
new_map.put("a", 6)


# for visualizing separate chaining
new_map2 = HashMap()
print("Number of items ", new_map2.get_size())
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("litecoin", 257.68)
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("cardano", 0.911735)
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("ethereum", 1182.28)
print("Number of items ", new_map2.get_size())
new_map2.return_capacity()
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("iota", 3.89)
new_map2.return_capacity()
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("ripple", 2.50)
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("dogecoin", 7)
print("Number of items ", new_map2.get_size())
new_map2.print_table()
new_map2.return_capacity()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("tron", 0.155263)
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("raiblocks", 25.65)
print("Number of items ", new_map2.get_size())
new_map2.print_table()
print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
new_map2.put("bitcoin", 15364.70)
new_map2.print_table()
new_map2.return_capacity()
print("Number of items ", new_map2.get_size())