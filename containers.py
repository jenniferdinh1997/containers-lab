# Exercise 1:
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['Bob', 'John', 'Bill']
print(students[1])
print(students[-1])

# Exercise 2:
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".
food = ('cheese', 'macaroni', 'bacon')
for item in food:
    print(f'{item} is a good food')

# Exercise 3:
# Using a for loop, print just the last two food strings from foods.
food = ('cheese', 'macaroni', 'bacon')
for position in range(len(food)-1,0,-1):
    print(food[position])

# Exercise 4:
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
    'city': 'Westminster',
    'state': 'CA',
    'population': 91000
}

print(f"I was born in {home_town['city']},{home_town['state']} - population of {home_town['population']}")

# Exercise 5:
# Iterate over the key: value pairs in home_town and print a string for each item
for key,val in home_town.items():
    print(f"{key} = {val}")

# Exercise 6:
# Create an empty list named cohort.
# Using a for loop, add one dictionary to the cohort list for each student name
# Iterate over cohort printing out each element.
cohort = []
for idx,student in enumerate(students): 
    cohort.append({'student': student, 'fav_food': food[idx]})
    print(idx,student)

for student in cohort:
    print(student)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list
# Iterate over awesome_students printing out each string.
awesome_students = [student for student in students]

for student in awesome_students:
    print(f'{student} is awesome!')

# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.
a_foods = [food for food in food if 'a' in food]
for food in a_foods:
    print(food)