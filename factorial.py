"""Module for function factorial"""
def factorial(num:int):
	result = num
	try: 
		if num < 0:
			return "This function only accepts non-negative numbers"
		if num in (0,1):
			return result
	
		while num != 2:
			result *= (num-1)
			num -= 1
		
		return result
	except TypeError:
		return "TypeError : Not a positive integer"