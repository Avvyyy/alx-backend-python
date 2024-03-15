#!/usr/bin/env python3
"""Program to return the returns the sum of a group of numbers as a float"""


from typing import List, Union
#Type-annotated function that takes a group of numbers and returns their sum as a float

def sum_mixed_list(mxd_lst: List[Union[int, str]]) -> float:
	"""
		Function that returns the sum of a group of numbers as a float

		Arg:
			mxd_lst: int | float

		Return:
			sum of alle elements in mxd_lst
	"""
	sum: int = 0
	for el in mxd_lst:
		sum += el

	return float(sum)