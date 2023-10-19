import os
import openai
#loaded our environment variables

from dotenv import load_dotenv, find_dotenv
_= load_dotenv(find_dotenv())# read local .env file

openai.api_key=os.environ["OPENAI_API_KEY"]

from langchain.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate

#2
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory 

#1
# from langchain.schema import(
#     SystemMessage,
#     HumanMessage,
#     AIMessage
# )

# chat=ChatOpenAI(temperature=0.9)

# messages=[
#     SystemMessage(content="You are a helpful assistant")
    
# ]

#2
# llm = ChatOpenAI()
# conversation=ConversationChain(
#     llm=llm,
#     memory=ConversationBufferMemory(),
#     verbose=False
# )
# print("Hello,I am chatBot!")

#1
# while True:
#     user_input = input(">")

#     # print("You sent: ",user_input)
#     messages.append(HumanMessage(content=user_input))

#     ai_response=chat(messages)

#     messages.append(AIMessage(content=ai_response.content))

#     print("\nAssistant:\n", ai_response.content)

#     print("History:",messages)

#2
# while True:
#     user_input = input(">")

#     ai_response=conversation.predict(input=user_input)

#     print("\nAssistant:\n", ai_response)

from flask import Flask, render_template, request, jsonify,send_from_directory
app = Flask(__name__)
# Route to serve the index.html file
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return "Not Found", 404

# Initialize the chatbot (same as in your previous code)
llm = ChatOpenAI()
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferMemory(),
    verbose=False
)

@app.route('/api/chat', methods=['POST'])  # Corrected the route
def chat():
    user_input = request.json.get('message', '')
    if user_input:
        # Predict a response from the chatbot based on user input
        ai_response = conversation.predict(input=user_input)
        return jsonify({'message': ai_response})
    else:
        return jsonify({'message': 'Invalid input'})

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for better error messages
