# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:30:08 2024

@author: Dell
"""

def plusMinus(arr):
    # Write your code here
    length= len(arr)
    #print(length)
    positive_num= [num for num in arr if num > 0]
    negative_num=[num for num in arr if num < 0]
    zero_num= [num for num in arr if num == 0]
    
    positive_count= len(positive_num)
    negative_count= len(negative_num)
    #print(negative_count)
    zero_count= len(zero_num)
    #print(zero_count)
    
    positive_ratio = round(positive_count / length, 6)
    negative_ratio = round(negative_count / length, 6)
    zero_ratio = round(zero_count / length, 6)
    
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)
    

print(plusMinus([1,1,0,-1,-1]))
