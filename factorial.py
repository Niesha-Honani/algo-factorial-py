def factorial(num):
	if num < 0:
		return "This function only accepts non-negative numbers"
	elif num == 0 or num == 1:
		return 1
	
	return num * factorial(num-1)
