import os
import openai
#loaded our environment variables

from dotenv import load_dotenv, find_dotenv
_= load_dotenv(find_dotenv())# read local .env file

openai.api_key=os.environ["OPENAI_API_KEY"]

# Getting request from OpenAI

# def get_completion(prompt,model="gpt-3.5-turbo"):
#     messages = [{"role":"user","content":prompt}]
#     response= openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=1
#     )

#     return response.choices[0].message["content"]

# response=get_completion("What is 1+1")
# print(response)

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

response=ChatOpenAI(temperature=1)
# print(response)

# customer_email="Hey ! Where are you? Why did you miss board meeting. Come right now we need to talk. You behaviour to miss the meeting was very disgusting"

# customer_style="Indian English in a very calm and respectful tone"

# prompt="""Translate the text that delimited by triple backticks into a style that is {style}, text : ```{text}```"""

# prompt_template = ChatPromptTemplate.from_template(prompt)

# customer_message = prompt_template.format_messages(
#     style=customer_style,
#     text=customer_email
# )

# customer_response=response(customer_message)
# print(customer_response)

# chat_model=ChatOpenAI()
# ans= chat_model.predict("1+1")
# print(ans)

# Remembering the chat History

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory 

memory = ConversationBufferMemory()

conversation=ConversationChain(
    llm=response,
    memory=memory,
    verbose=False
)

# res1=conversation.predict(input="Hi, My name is Saloni")

# res2=conversation.predict(input="What is 1+1")
# res3=conversation.predict(input="What is my name")

# print(memory.buffer)

# print(memory.load_memory_variables({}))


from langchain.memory import ConversationBufferWindowMemory
memory=ConversationBufferWindowMemory(k=1)

memory.save_context({'input':"Hi"},{"output":"What's up"})

memory.save_context({"input":"Nothing Much"},{"output":"Cool"})

print(memory.load_memory_variables({}))

