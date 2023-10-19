def generate_fibonacci(n):
    fib = []
    if n <= 0:
        return fib
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            next_number = fib[-1] + fib[-2]
            fib.append(next_number)
        return fib

# Using fib[-1] and fib[-2]: 
# In Python, you can use negative indices to access elements from the end of a list.
# fib[-1] refers to the last element in the list (fib[-1] is equivalent to fib[len(fib) - 1]), 
# and fib[-2] refers to the second-to-last element in the list (fib[-2] is equivalent to fib[len(fib) - 2]).

# Test the function
input_n = 5
result = generate_fibonacci(input_n)
print(result)
