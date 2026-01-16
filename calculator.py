def multiply(a, b):
	return a * b


def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def divide(a, b):
	return a / b


def square(x):
	return x * x


def cube(x):
	return x * x * x


def square_n_times(number, n):
	"""Square `number` repeatedly `n` times and return the sum.

	On each iteration, the current value is squared and added to the total.
	For example, with number=2 and n=3:
	- iteration 1: 2^2 = 4
	- iteration 2: 4^2 = 16
	- iteration 3: 16^2 = 256
	Sum returned: 4 + 16 + 256 = 276

	If `n` is 0, returns 0. Expects non-negative integer `n`.
	"""
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	result = 0
	current = number
	for _ in range(n):
		current = current * current
		result += current
	return result