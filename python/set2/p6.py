# Given lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# Initialize an empty list to store the result
result = []

# Nested loop to concatenate elements from both lists
for item1 in list1:
    for item2 in list2:
        result.append(item1 + item2)

# Print the result
print(result)
