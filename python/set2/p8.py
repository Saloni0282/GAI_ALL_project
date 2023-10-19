# Given employees list and defaults dictionary
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Initialize the dictionary with default values
result = {employee: defaults.copy() for employee in employees}

# Print the result
print(result)
