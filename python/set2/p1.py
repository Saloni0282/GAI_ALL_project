# Define the number of rows for the pattern
num_rows = 5

# Outer loop for rows
for i in range(1, num_rows + 1):
    # Inner loop for numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")  # Print the number with a space
    print()  # Move to the next line after each row
