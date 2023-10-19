import csv
import jsonlines

# Define the input CSV file and output JSONL file names
csv_file = 'test.csv'
jsonl_file = 'test.jsonl'

# Define the constant system prompt
system_prompt = "Replicate the tone of the answer given by the assistant"

# Open the CSV file for reading and the JSONL file for writing
with open(csv_file, 'r', newline='', encoding='utf-8') as csv_in_file, \
     jsonlines.open(jsonl_file, mode='w') as jsonl_out_file:

    # Create a CSV reader
    csv_reader = csv.DictReader(csv_in_file)

    for row in csv_reader:
        # Extract the question and answer from the CSV row
        question = row['Question']
        answer = row['Answer']

        # Create the JSONL data structure
        json_data = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer}
            ]
        }

        # Write the JSON data to the JSONL file
        jsonl_out_file.write(json_data)

print(f'Conversion completed. JSONL file "{jsonl_file}" created.')







