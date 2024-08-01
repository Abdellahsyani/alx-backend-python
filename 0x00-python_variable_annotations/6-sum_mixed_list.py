#!/usr/bin/env python3
'''the annotation of mixed list of float and integer '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''return the sum list of integer and float numbers as a float'''
    return sum(mxd_lst)
