# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:06:07 2024

@author: Dell
"""

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        
        spaces='' * (n - i)
        hashes= '#' * i
        
        print(spaces + hashes.rjust(n))
        
        
staircase(6)