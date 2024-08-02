#number Guessing game
import random
rand_num = random.choice(range(1,11))
mainloop = True
while mainloop:
    entery = int(input("guess the number: "))
    if entery == rand_num:
        print("You win!")
        mainloop = False
    else:
        print("try again")
