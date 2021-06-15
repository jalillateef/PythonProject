#Ask the user for their name
name = input("Enter name: ")

#Welcome the user
print(name + ", welcome to Guess The Number!")

#Give the user instructions for the game
print("""Instructions: The object of the game is to guess the secret number from 1-10. 
    You have a total of 7 guesses. You will get a new hint every time you guess wrong.""")

    #Ask the user if they are ready
while True:
    answer = input("Are you ready? Reply Yes or No: ").lower()
    if answer.startswith('y'):
        print("Great!")
        break
    if answer.startswith('n'):
        print("Well you better get ready!")
        break
    else:
        print("You have to choose Yes or No.")
        break

#Def a function to wrap the game in
def game():
    #Import the random module (To generate random numbers between 1 - 100)
    import random

    #Set the random number range
    number = random.randint(1, 10)

    #Set the number of starting guesses
    guesses_remaining = 7

    #Give a while loop that is true
    while guesses_remaining < 8 and guesses_remaining != 0:
        try:
            guess = int(input("I'm thinking of a number from 1 to 10, take a guess: "))
        except ValueError:
            print("Try again. Please enter a valid number.")

    #Have the 'guesses remaining' to minus 1 every wrong guess by the user
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
        
        #If neither while condition is true
        if guesses_remaining == 0:
            print("YOU LOSE!")
        #Convert number variable into a string to concotenate it and print
            number = str(number)
            print("The number I had in mind was " + number + ".")
            break



    #Give the user option to restart game by calling the function
    restart = input("Would you like to play again? Reply yes or no: ")
    if restart.startswith("y"):
            game()
    if restart.startswith("n"):
            print("Goodbye.")
game()





