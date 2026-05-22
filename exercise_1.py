my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]

# Write a program that prints out all the elements of the list that are higher than or equal to 10.
for number in my_list:
    if number >= 10:
        print(number)

# Instead of printing the elements one by one,
# make a new list that has all the elements higher than or equal to 10 from this list in it and print out this new list.

new_list = []

for number in my_list:
    if number >= 10:
        new_list.append(number)
print(new_list)

#Ask the user for a number as input and print a list that contains only those elements from my_list that are higher
# than the number given by the user.

list_two = []
user_input = input("Dear user, please enter some random number:\n")
for number in my_list:
    if int(user_input) < number:
        list_two.append(number)
print(list_two)
