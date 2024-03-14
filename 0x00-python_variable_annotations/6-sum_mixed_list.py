from typing import List, Union
#Type-annotated function that takes a group of numbers and returns their sum as a float

def sum_mixed_list(mxd_lst: List[Union[int, str]]) -> float:
	sum: int = 0
	for el in mxd_lst:
		sum += el

	return float(sum)