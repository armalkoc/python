import random

# we want user input and run the program as long as we have valid user input

def guess_number(user_input, random_num):

        if user_input.isnumeric():
            if int(user_input) == random_num:
                print(f"You guessed the number {random_num} and YOU WON !!!")
            elif int(user_input) < random_num:
                print("You guessed too low !!!")
            else :
                print("You guessed too high !!!")
        else:
            print("Your entry is not number")

while True:
    random_num = random.randint(1, 9)
    user_input = input("Dear user, please try to guess the number between 1 and 9:\n")

    if user_input in ['exit', 'quit', 'q']:
        print("You stopped the game !!!")
        break
    else:
        guess_number(user_input, random_num)