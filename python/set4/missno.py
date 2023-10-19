def missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    return total_sum - sum(nums)

# Test
nums = [3, 0, 1]
print(missing_number(nums))  # Output: 2
