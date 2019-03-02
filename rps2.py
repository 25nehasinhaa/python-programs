import random
#take choice from user
l=['r','p','s']

di={'r':"rock",'p':"paper",'s':"scissor"}

usc=0
csc=0


while True:

	u= input("Enter your choice r/p/s >")

	#take choice from comp
	c= random.choice(l)

	print("user chose",di[u])
	print("computer chose",di[c])
	if u==c:
		print('its a tie')
	 
   	elif u=='r' and c=='s':
		print("u is the winner")
		usc=usc+1

	elif u=='s' and c=='p':
		print("u is the winner")
		usc=usc+1

	elif u=='p' and c=='r':
		print("u is the winner")
		usc=usc+1

	else:
		print("Computer wins")
		csc=csc+1

	print("Score")
	print("Computer:",csc,"User",usc)
	if csc==3:
		print("Computer is the champion")
		exit()
	elif usc==3:
		print("User is the champion")
		exit() 		