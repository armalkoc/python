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

# print name, job and city for each employee in the dictionary
for person in employees:
    print(f"Name: {person['name']}")
    print(f"Job: {person['job']}")
    print(f"City: {person['address']['city']}")
    print("--------------------")

# country of the 2nd employee in the list

print(employees[1]["address"]["country"])  