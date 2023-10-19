def two_sum(nums, target):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None

# Test the function with the given input
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


# def two_sum(nums, target):
#     n = len(nums)
#     result = []
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 result.append([i, j])
    
#     return result if result else None

# # Test the function with the given input
# nums = [2, 7, 11, 15, 4, 5]
# target = 9
# result = two_sum(nums, target)
# print(result)  # Output: [[0, 1], [4, 5]]

