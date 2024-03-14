from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
	def multiplierFunction(a: float) -> float:
		return a * multiplier

	return multiplierFunction 