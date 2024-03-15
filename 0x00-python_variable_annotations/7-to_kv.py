#!/usr/bin/env python3

from typing import List, Union
#Type annotated function to return a tuple of a string and a number
def to_kv(k: str, v: List[Union[int, float]]) -> tuple:
	return (k, v**2)