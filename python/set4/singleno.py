def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test
nums = [4, 1, 2, 1, 2]
print(single_number(nums))  # Output: 4
