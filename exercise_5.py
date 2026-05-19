def calculator(number1, number2, operation):
    match operation:
        case "plus":
            print(number1 + number2)
        case "minus":
            print(number1 - number2)
        case "multiply":
            print(number1 * number2)
        case "divide":
            print(number1 / number2)

num_of_calculations = 0
while True:
    num1 = input("Dear user please enter the number1:\n")

    # check user entry is number1
    if num1 == 'exit':
        print("Your input is not number !")
        print(f"You did {num_of_calculations} calculations")
        break

    num2 = input("Dear user please enter the number2:\n")

    # check if user entry is valid number2
    if num2 == 'exit':
        print("Your input is not number !")
        print("You did {num_of_calculations} calculations")
        break

    # check if these entries are valid numbers not any other kind of entry
    valid_numbers = num1.isnumeric() or num2.isnumeric()

    operation = input("Dear user, please enter an operation you want to perform (plus, minus, divide or multipy):\n")
    valid_operation = operation == "plus" or operation == "minus" or operation == "divide" or operation == "multiply"

    if not valid_numbers:
        print("Sorry, only numbers are allowed")
    elif not valid_operation:
        print("Sorry, only +,-,*,/ are allowed")
    else:
        calculator(int(num1), int(num2), operation)
        num_of_calculations += 1
        print(f"Your calculation has been made {num_of_calculations} times")






