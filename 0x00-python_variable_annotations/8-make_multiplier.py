#!/usr/bin/env python3
'''the multiplier annotation function '''
from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''using Callable to return the multiplier of number'''
    def multiply(number: float) -> float:
        '''the helper function to let the callable work'''
        return number * multiplier
    return multiply
