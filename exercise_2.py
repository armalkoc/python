# dictionary
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Update the job to the Software Engineer
"""employee.update({"job": 'Software Engineer'})
print(employee)"""

employee["job"] = "Software Engineer"
print(employee)

# Remove the age key from the dictionary
employee.pop("age")
print(employee)

# List key:value pairs
for key, value in employee.items():
  print(f"{key}:{value}")