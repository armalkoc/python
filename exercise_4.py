from helper import print_employee_age_name, calculate_upper_and_lower_letters, print_even_numbers

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

print_employee_age_name(employees)

user_input = input("Dear user, please enter some random string that includes upper and lower letters:\n")
calculate_upper_and_lower_letters(user_input)

user_num = input("Dear user please enter the list of the numbers:\n")
numbers_list = [int(num) for num in user_num.split()]
print_even_numbers(numbers_list)





















