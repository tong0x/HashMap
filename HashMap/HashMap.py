#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:19:16 2018

@author: Tong Pow

Implementation of HashMap using separate chaining. 

"""

class HashMap:
    
    # Initialize Hashtable as a list of lists with its iniital capacity as 2
    def __init__(self):
        self.capacity = 2
        self.num_items = 0
        self.load_factor = 0.75 # load factor to determine threshold for table size
        self.table = [None for x in range(self.capacity)]
    
    # for customizing load factor which determines when to resize table
    def set_load_factor(self, new_factor):
        self.load_factor = new_factor
        
    
    # Hash function to assign index value to store value in the table
    def hash_it(self, key):
        index = hash(key) % self.capacity
        return index
    
    # check whether resize is needed
    def should_resize(self):
        if self.num_items > self.load_factor * self.capacity:
            return True
        return False
    
    # check table capacity to see whether resize is needed, and place item on hashtable
    def put(self, key, value, resizing=False):
        if self.should_resize(): 
            self.resize_table(2, self.capacity)
        index = self.hash_it(key)
        if self.contains_key(key):
            for i, kv in enumerate(self.table[index]):
                k, v = kv
                if k == key:
                    self.table[index][i] = (key, value)
        else: 
            if self.table[index] == None:
                self.table[index] = [(key, value)]
            else:
                self.table[index].append((key, value))
            if resizing == False:
                self.num_items += 1
    
    # look up and return value through obtaining index using hash function and iterate to find key.
    # return None if value not found
    def get_value(self, key):
        index = self.hash_it(key)
        if self.contains_key(key):
            target_list = self.table[index]
            for k, v in target_list:
                if k == key:
                    return v
        else: 
            return None
        
   # check if key is present in HashMap
    def contains_key(self, key):
        index = self.hash_it(key)
        if self.table[index] == None:
            return False
        else:
            target_list = filter(None, self.table[index])
            for kv in target_list:
                k, v = kv
                if (key == k):
                    return True
        return False
        
    
    # iterate through entire table to check if value is present in HashMap
    def contains_value(self, value):
        for curr_list in self.table:
            if curr_list == None:
                continue
            for k, v in curr_list:
                if value == v:
                    return True
        return False
    
    # check if key is in table, and remove accordingly
    def remove(self, key):
        if self.contains_key(key):
            index = self.hash_it(key)
            for k, v in self.table[index]:
                if key == k:
                    self.table[index].remove((k, v))
                    self.num_items -= 1
                    # if the bucket at the target index is an empty list, set it to None
                    if self.table[index] == []:
                        self.table[index] = None
                    return 
        return
    
    # make new table of capacity changed by resize_factor, and rehash all items 
    def resize_table(self, resize_factor, table_capacity):
        self.capacity *= resize_factor
        old_table = self.table
        self.table = [None for x in range(self.capacity)]
        # rehash all items from old table to new table with new capacity
        for curr_list in old_table:
            if curr_list == None:
                continue
            for pair in curr_list:
                k, v = pair
                self.put(k, v, resizing=True)
    
    # for testing
    def print_table(self):
        print(self.table)
    def return_capacity(self):
        print("Current capacity ", self.capacity)
    def get_size(self):
        return self.num_items
    
    
                
        
        
    
    