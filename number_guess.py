import random

random_number= random.randint(1,100)
guess = input()

print ("Guess the number between 1 to 100")



if guess > random_number:
    print("decrease the number")
elif guess < random_number:
    print ("increase the number")
else:
    print ("the number is:",random_number)

