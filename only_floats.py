def only_floats(num1,num2):

	if type(num1) == float and type(num2) == float:
		return 2
	elif type(num1) == float or type(num2) == float:
		return 1
	else:
		return 0


print(only_floats(1,1))