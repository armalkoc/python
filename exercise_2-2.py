dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

# merges two python dictionaries into one new dictionary

"""merged_dict = dict_one | dict_two
print(merged_dict)"""

merged_dict = dict_one.copy()
merged_dict.update(dict_two)
print(merged_dict)

# sums up all the values in the new dictionary and print it up
"""result = sum(merged_dict.values())
print(result)"""

summary = 0
for value in merged_dict.values():
    summary = summary + value
print(summary)

# minimum and maximum value of the dictionary values
dict_one = {'a': 100, 'b': 400}
dict_two = {'x': 300, 'y': 200}

dict_merged = dict_one.copy()
dict_merged.update(dict_two)
print(dict_merged)

merged_values = []
for value in dict_merged.values():
    merged_values.append(value)

merged_values.sort()
print(merged_values)
print(len(merged_values))
print(f"Minimum value is: {merged_values[0]}")
print(f"Maximum values is {merged_values[-1]}")