# Initialize an empty dictionary
people_dict = {}

# Function to add a new name-age pair
def add_person(name, age):
    people_dict[name] = age

# Function to update the age of a name
def update_age(name, new_age):
    if name in people_dict:
        people_dict[name] = new_age

# Function to delete a name from the dictionary
def delete_person(name):
    if name in people_dict:
        del people_dict[name]

# Print the initial empty dictionary
print(people_dict)  # Output: {}

# Add a new name-age pair
add_person("John", 25)
print(people_dict)  # Output: {'John': 25}

# Update the age of "John"
update_age("John", 26)
print(people_dict)  # Output: {'John': 26}

# Delete "John" from the dictionary
delete_person("John")
print(people_dict)  # Output: {}
