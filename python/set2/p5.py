# Given lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Initialize an empty list to store the result
result = []

# Iterate through both lists simultaneously using zip
for item1, item2 in zip(list1, list2):
    # Concatenate the elements index-wise and append to the result list
    result.append(item1 + item2)

# Add any leftover items from the longer list to the result
if len(list1) > len(list2):
    result.extend(list1[len(list2):])
elif len(list2) > len(list1):
    result.extend(list2[len(list1):])

# Print the result
print(result)
