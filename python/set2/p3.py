# Given strings
s1 = "Ault"
s2 = "Kelly"

# Calculate the middle index of s1
middle_index = len(s1) // 2

# Create the new string s3 by inserting s2 in the middle of s1
s3 = s1[:middle_index] + s2 + s1[middle_index:]

# Print the result
print(s3)
