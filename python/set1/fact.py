def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

# Test the function
input_number = 5
result = calculate_factorial(input_number)
print(f"Factorial of {input_number} is {result}.")
