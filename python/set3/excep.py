def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Test the function with the given input
num1 = 5
num2 = 0
result = safe_divide(num1, num2)
print(result)  # Output: "Cannot divide by zero."
