#!/usr/bin/env python3
"""Function that returns the length of 2 numbers"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Function that returns a tuple of lengths

        Args:
            lst: List

        Return:
            a tuple
    
    """
    return [(i, len(i)) for i in lst]