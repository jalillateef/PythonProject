#Ask the user for their name
name = input("Enter name: ")

#Welcome the user
print(name + ", welcome to Guess The Number!")

#Give the user instructions for the game
print("""Instructions: The object of the game is to guess the secret number from 1-100. 
You have a total of 7 guesses. You will get a new hint every time you guess wrong, but
your number og guesses will be reduced by 1.""")

#Ask the user if they are ready
while True:
    answer = input("Are you ready? Reply Yes or No: ").lower()
    if answer.startswith('y'):
        print("Great!")
        break
    elif answer.startswith('n'):
        print("Well you better get ready!")
        break
    else:
        print("You have to choose Yes or No.")

import random
n = random.randint(1, 99)
tries_left = 6
guess = int(input("Enter an integer from 1 to 100: "))
while n != guess:
    if guess > n:
        print("Too high, try again.")
        tries_left -= 1
        print ("Tries left: " + str(tries_left))
        guess = int(input("Enter an integer from 1 to 100: "))
    # elif guess < n:
        












#Ask user if they are ready

# answer = input('Are you ready? Reply yes or no:').lower()
# if answer.startswith('y'): 
#     print("Great!") 
# elif answer.startswith('n'):
#     print("Well you better get ready!")
# else:
#     print("Sorry I didn't understand that.")
        




