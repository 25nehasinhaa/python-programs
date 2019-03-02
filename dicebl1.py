for i in range(1,7):
    r=input("Press r to roll, q to quit : ")

    if r=='r':
        if i%3 == 1:
            print("You got",6)

        elif i%3 == 2:
            print("You got",2)

        else:
            print("You got",3)

    if r == 'q':
        print("Bye,Nihal!")
        exit()

print("Congratulations, you won!")        
            
            