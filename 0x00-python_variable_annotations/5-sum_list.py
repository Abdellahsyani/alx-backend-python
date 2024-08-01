#!/usr/bin/env python3
'''function to return the list of floats'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return the sum of float list '''
    summ = 0
    for i in input_list:
        summ += i
    return (summ)
