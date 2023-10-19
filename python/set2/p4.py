# Given string
str1 = "PyNaTive"

# Initialize strings for lowercase and uppercase letters
lowercase_letters = ""
uppercase_letters = ""

# Iterate through the characters in the string
for char in str1:
    if char.islower():
        # Append lowercase letters to the lowercase string
        lowercase_letters += char
    elif char.isupper():
        # Append uppercase letters to the uppercase string
        uppercase_letters += char

# Concatenate the lowercase and uppercase strings
result = lowercase_letters + uppercase_letters

# Print the result
print(result)
