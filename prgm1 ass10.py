1#open a file with try and except
def divide(x,y):
	try:
		result=x//y
		print("yeah ! your answer is:",result)
	except ZeroDivisionError:
		print("Sorry ! you are dividing by zero")
divide(3,0)
	