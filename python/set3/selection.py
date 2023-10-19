def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the function with the given input
input_array = [64, 25, 12, 22, 11]
selection_sort(input_array)
print(input_array)  # Output: [11, 12, 22, 25, 64]
