# Given list of numbers
numbers = [12, 75, 150, 180, 145, 525, 50]

# Iterate through the list and apply conditions
for num in numbers:
    # Check if the number is divisible by five
    if num % 5 == 0:
        # Check if the number is greater than 150
        
        # Check if the number is greater than 500
        if num > 500:
            break;  # Stop the loop
        if num > 150:
            continue  # Skip numbers greater than 150
        # If none of the above conditions are met, print the number
        print(num)
