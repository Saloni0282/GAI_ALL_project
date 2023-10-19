def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

# Test
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"
