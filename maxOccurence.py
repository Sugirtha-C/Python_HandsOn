# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:25:42 2024

@author: Dell
"""

#count occurences of tallest candle

def birthdayCakeCandles(candles):
    # Write your code here

    max_candles=max(candles)
    return candles.count(max_candles)

print(birthdayCakeCandles([3,3,1,2]))