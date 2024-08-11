# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:14:13 2024

@author: Dell
"""

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum=sum(arr[:4])
    max_sum=sum(arr[-4:])
    print(min_sum, max_sum)
    
miniMaxSum([1,9,3,4,5])