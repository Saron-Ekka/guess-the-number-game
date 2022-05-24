print("----------GUESS THE NUMBER GAME----------")
def game():
    print("Do you want to play?")
    play= str(input()).lower()
    if play == "no":
        quit()
    elif play == "yes":
        print("okay! let's play :)")
    else:
        print("wrong input")
        game()
game()


import random
a=random.randint(1,20)
x=True

for i in range(1,6):
    print("Choose a no. between 1 to 20")
    b= int(input())
    if b>20:
        print("your choice was not in the range")
    elif b==a:
        x=True
        print("Right guess in " + str(i) + " turns.")
        break
    elif b>a:
        x=False
        print("Your guess is high")
    elif b<a:
        x=False
        print("your guess is low")
if x==False:
    print("right answer was " + str(a))












