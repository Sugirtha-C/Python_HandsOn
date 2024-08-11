# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:45:14 2024

@author: Dell
"""

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
   
   #alice_points=sum(1 for x, y in zip(a,b) if x >y)
   #bob_points=sum(1 for x,y in zip(a,b) if y >  x)
   
 a_np=np.array(a)
 b_np=np.array(b)
 
 alice_points= np.sum(a_np > b_np)
 bob_points=np.sum(b_np > a_np)
 
 return [alice_points,bob_points]
 
   
print(compareTriplets([1,2,3],[8,2,1]))

 