# Given lists
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Iterate through both lists simultaneously using zip
for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)

# # Given lists
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# # Get the reversed version of list2
# reversed_list2 = list2[::-1]

# # Iterate through list1 and reversed_list2 manually
# for i in range(len(list1)):
#     print(list1[i], reversed_list2[i])
