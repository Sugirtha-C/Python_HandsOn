# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:14:23 2024

@author: Dell
"""
import numpy as np


def diagonaldifference(matrix):
    np_matrix=np.array(matrix)
    main_diag_sum= sum(np_matrix.diagonal())
    anti_diag_sum=sum(np_matrix[:,::-1].diagonal())
    absolute= abs(main_diag_sum - anti_diag_sum)
    return absolute


#### non-numpy method
# n = len(matrix)
   # main_diag_sum = sum(matrix[i][i] for i in range(n))
   # anti_diag_sum = sum(matrix[i][n - i - 1] for i in range(n))
    
    ###

matrix_array= [
    [11 ,2 ,4],
    [4, 5, 6],
    [10, 8 ,-12]
    ]

print(diagonaldifference(matrix_array))
    