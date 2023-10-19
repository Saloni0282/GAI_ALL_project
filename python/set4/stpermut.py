from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Test
s = "abc"
print(string_permutations(s))
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
