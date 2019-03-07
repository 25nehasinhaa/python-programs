def func1():
	print("hii")
	print("hello")

func1()	


def func2(a):
	print("Hi\t",a)

def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)	

def func4(university= "IITB"):
	print("I am in" +"\t" + university)
func4("IITG")
func4("IITD")
func4()

def func5(a,b):	
	print("hii other function")
	c=a+b	
	return c

def func6():
	print("hello")
	s=func5(2,7)
	print("addition is", s)
		