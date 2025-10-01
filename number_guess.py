import random

random_number= random.randint(1,100)
guess=None

while guess!=random_number:
    print ("enter the number you guess")
    guess = int (input())
    if guess > 100 or guess < 1:
        print("please enter number between 1 and 100")
    elif guess > random_number:
        print("decrease the number")
    elif guess < random_number:
        print ("increase the number")
    else:
        print ("Congratulations! you guess is right, the number is",random_number)

