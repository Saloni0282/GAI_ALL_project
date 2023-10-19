# def reverse_string(input_string):
#     # Use string slicing with a step of -1 to reverse the string
#     reversed_string = input_string[::-1]
#     return reversed_string


def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

# Test the function
input_string = "Python"
reversed_result = reverse_string(input_string)
print(reversed_result)
