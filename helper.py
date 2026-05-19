# Write a function that accepts a list of dictionaries with employee age
# and prints out the name and age of the youngest employee.

def print_employee_age_name(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

        print(f"Name of the youngest employee: {youngest_employee_name}")
        print(f"Age of the youngest employee: {youngest_employee_age}")

# Write a function that accepts a string and calculates the number of upper case letters and lower case letters

def calculate_upper_and_lower_letters(user_input):
    upper_letters = 0
    lower_letters = 0
    for letter in user_input:
        if letter.isupper():
            upper_letters += 1
        elif letter.islower():
            lower_letters += 1
    print(f"Number of upper letters is: {upper_letters}")
    print(f"Number of lower letters is: {lower_letters}")

#user_input = input("Dear user, please enter some random string that includes upper and lower letters:\n")

# Write a function that prints the even numbers from a provided list

"""user_num = input("Dear user please enter the list of the numbers:\n")
numbers_list = [int(num) for num in user_num.split()]
print(numbers_list)"""

def print_even_numbers(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(f"Even number is: {number}")