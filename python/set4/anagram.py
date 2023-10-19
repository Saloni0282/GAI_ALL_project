def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)

# Test
print(is_anagram("cinema", "iceman"))  # Output: True
