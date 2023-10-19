import os

import openai

from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.environ.get('OPENAI_API_KEY')

# with open("./test.jsonl", "rb") as file:
#     response =openai.File.create(
#         file=file,
#         purpose='fine-tune'    
#     )
# file_id=response["id"]

# print(f"File uploaded by id : {file_id}")

file_id="file-ZY2zVDeUJ7Czx2tFf4kT0fJ1"
model_name="gpt-3.5-turbo"

response=openai.FineTuningJob.create(
    training_file=file_id,
    model=model_name
)

job_id=response["id"]
print(f"Fine tunning job create with id : {job_id}")