#!/usr/bin/env python3
"""Program that returns the sum of the numbers in a list"""
#Type-annotated function that returns teh sum of floating point numbers

def sum_list (input_list: list) -> float:
	"""
		Function that computes the sum of items in a list

		Arg:
			input_list

		Return:
			The sum of all the items in input_list
	"""
	sum: int = 0
	for item in input_list:
		sum += item
	
	return sum