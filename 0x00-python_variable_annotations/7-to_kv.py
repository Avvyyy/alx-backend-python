#!/usr/bin/env python3
"""Program to return a tuple of a string anf value"""


from typing import List, Union


#Type annotated function to return a tuple of a string and a number
def to_kv(k: str, v: List[Union[int, float]]) -> tuple:

	"""
		Function to return a tuple

		Args:
			k: String
			v: a number

		Return:
			Tuple(k, v)
	"""
	
	return (k, v**2)