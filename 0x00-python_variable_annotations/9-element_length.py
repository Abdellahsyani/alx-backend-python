#!/usr/bin/env python3
'''the value appropriate'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Processes an iterable of sequences, returning the original iterable"""
    lengths = [(item, len(item)) for item in lst]
    return lst, lengths
