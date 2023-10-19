def is_prime(number):
    # Check if the number is less than 2 (prime numbers are greater than 1)
    if number < 2:
        return False
    
    # Iterate from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by any integer in this range, it's not prime
        if number % i == 0:
            return False
    
    # If the loop completes without finding a divisor, the number is prime
    return True

# Test the function
input_number = 13
if is_prime(input_number):
    print(f"{input_number} is a prime number.")
else:
    print(f"{input_number} is not a prime number.")
