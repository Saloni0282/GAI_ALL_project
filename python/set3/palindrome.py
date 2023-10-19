def is_palindrome(word):
    # Remove spaces and convert the word to lowercase for accurate comparison
    cleaned_word = "".join(word.split()).lower()
    
    # Initialize pointers for the start and end of the cleaned word
    start = 0
    end = len(cleaned_word) - 1
    
    while start < end:
        if cleaned_word[start] != cleaned_word[end]:
            return f"The word '{word}' is not a palindrome."
        start += 1
        end -= 1
    
    return f"The word '{word}' is a palindrome."

# Test the function with the given input
input_word = "madam"
result = is_palindrome(input_word)
print(result)  # Output: "The word 'A man a plan a canal Panama' is a palindrome."


# def is_palindrome(word):
#     # Remove spaces and convert the word to lowercase for accurate comparison
#     cleaned_word = word.replace(" ", "").lower()
    
#     # Check if the cleaned word is equal to its reverse
#     if cleaned_word == cleaned_word[::-1]:
#         return f"The word {word} is a palindrome."
#     else:
#         return f"The word {word} is not a palindrome."

# # Test the function with the given input
# input_word = "madam"
# result = is_palindrome(input_word)
# print(result)  # Output: "The word madam is a palindrome."
