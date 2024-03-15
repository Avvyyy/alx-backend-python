#!/usr/bin/env python3

#Type-annotated function that returns teh sum of floating point numbers

def sum_list (input_list: list) -> float:
	sum: int = 0
	for item in input_list:
		sum += item
	
	return sum