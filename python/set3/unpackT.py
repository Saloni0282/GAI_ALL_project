# Define a list of tuples
people = [("John", 25), ("Jane", 30)]

# Iterate through the list and use tuple unpacking to print name and age
for person in people:
    name, age = person  # Tuple unpacking
    print(f"{name} is {age} years old.")
