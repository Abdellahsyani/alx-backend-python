#!/usr/bin/env python3
'''working with tuple'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return the tuple with sun of int and float'''
    return k, v ** 2
