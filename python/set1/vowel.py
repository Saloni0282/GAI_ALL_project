def count_vowels(input_string):
    # Define a set of vowels
    vowels = "AEIOUaeiou"

    # Initialize a count variable to keep track of the number of vowels
    vowel_count = 0

    # Iterate through the characters in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1

    # Print the count of vowels
    print(f"Number of vowels: {vowel_count}")

# Test the function
input_string = "Hello"
count_vowels(input_string)
