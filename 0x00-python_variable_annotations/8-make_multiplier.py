#!/usr/bin/env python3
"""Program that returns a function that multiplies 2 numbers"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
	"""
		Function that returbs a function

		Args:
			muliplier

		Return:
			A function
	"""
	def multiplierFunction(a: float) -> float:
		"""
		Function that muliplies 2 numbers

		Args:
			a

		Return:
			a * multiplier	
		"""
		return a * multiplier

	return multiplierFunction 