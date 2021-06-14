#Ask the user for their name
name = input("Enter name: ")

#Welcome the user
print(name + ", welcome to Guess The Number!")

#Give the user instructions for the game
print("""Instructions: The object of the game is to guess the secret number from 1-100. 
    You have a total of 7 guesses. You will get a new hint every time you guess wrong.""")

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

#Import the random module (To generate random numbers between 1 - 100)
import random

#Set the random number range
number = random.randint(1, 10)

#Set a variable for starting number of guesses
guesses_remaining = 7
while guesses_remaining < 8 and guesses_remaining != 0:
    guess = int(input("I'm thinking of a number from 1 to 10, take a guess: "))
    guesses_remaining -= 1

    if guess < number:
        print('Your guess is too low.')
        print ("guesses remaining " + str(guesses_remaining))

    if guess > number:
        print('Your guess is too high.')
        print ("guesses left: " + str(guesses_remaining))

    if guess == number:
        print("YOU WON!")
        break
    

if guesses_remaining == 0:
    print("YOU LOSE!")
    number = str(number)
    print("The number i had in mind was " + number + ".")
    



    
    #         #Ask the user to pick a number and then control flow.
    # guess = int(input("I'm thinking of a number from 1 to 10: "))
    # while n != guess:
    #     if guess > n:
    #             print("Too high, try again.")
    #             tries_left -= 1
    #             print ("Tries left: " + str(tries_left))
    #             guess = int(input("I'm thinking of a number from 1 to 10: "))
    #     elif guess < n:
    #             print("Too low, try again.")
    #             tries_left -= 1
    #             print ("Tries left: " + str(tries_left))
    #             guess = int(input("I'm thinking of a number from 1 to 10: "))
    #     if tries_left == 1:
    #             print("GAME OVER!!!")
            
    #     if guess == n:
    #             winner_play_again = input("WINNER! CONGRATULATIONS! Would you like to play again?")
    #             if winner_play_again.startswith('y'):
    #                 response = input()
    #             elif not winner_play_again.startswith('y'):
    #                 print("Goodbye!")
    #                 break
        


            
            
                












    #     #Ask user if they are ready

    #     # answer = input('Are you ready? Reply yes or no:').lower()
    #     # if answer.startswith('y'): 
    #     #     print("Great!") 
    #     # elif answer.startswith('n'):
    #     #     print("Well you better get ready!")
    #     # else:
    #     #     print("Sorry I didn't understand that.")
                




