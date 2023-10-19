# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

# Keys to extract
keys_to_extract = ["name", "salary"]

# Create a new dictionary with extracted keys
extracted_dict = {key: sample_dict[key] for key in keys_to_extract if key in sample_dict}

# Print the extracted dictionary
print(extracted_dict)
