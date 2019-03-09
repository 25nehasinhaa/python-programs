def func():
	a=int(input ("first number is "))
	b=int(input ("second number is "))
	c=int(input ("third number is "))
	if a==b and b==c:
		print("all are the same")
	elif a>b and a>c:
		print("first number is greater")
		return
	elif b>a and b>c:
		print("second number is greater")
		return
	elif c>a and c>b:
		print("third number is greater")
		return	
func()	
