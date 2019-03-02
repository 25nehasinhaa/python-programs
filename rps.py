import random
#take choice from user

u= input("Enter your choice")

#take choice from comp
c= random.choice('rps')

if u==c:
	print('its a tie')
 
elif u=='r' and c=='s':
	print("u is the winner")

elif u=='r' and c=='p':
	print("c is the winner")

elif u=='s' and c=='p':
	print("u is the winner")

elif u=='s'	and c=='r':
	print("c is the winner")

elif u=='p'	and c=='s':
	print("u is the winner")

elif u=='p' and c='r':
	print("c is the winner")
	