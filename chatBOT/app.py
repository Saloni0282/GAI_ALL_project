from flask import Flask, render_template, request, jsonify,send_from_directory
import os
import openai

openai.api_key = "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"

app = Flask(__name__)

# Route to serve the index.html file
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favicon.ico")
def favicon():
    return "Not Found", 404

# Route to handle POST requests to the /api route
# @app.route("/api", methods=["POST"])
# def chat_with_bot():
#     try:
#         user_message = request.json["message"]
        
#         # Send user's message to OpenAI API for processing
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {
#                 "role": "system",
#                 "content": "I want to make a chatBot using chatgpt api \nand regarding the script example which i provide also if user ask any question to interview answer user with relevent answer to their question "
#                 },
#                 {
#                 "role": "user",
#                 "content": "Hello"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": "Hello, I am Ayesha your assistant. How can i help you"
#                 },
#                 {
#                 "role": "user",
#                 "content": "Can you tell me about common interview questions?"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": "Certainly! Common interview questions often include behavioral questions like \"Tell me about yourself\" or technical questions related to your field of expertise. Do you have a specific type of question in mind?"
#                 },
#                 {
#                 "role": "user",
#                 "content": "What are some tips for a successful interview?"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": "Great question! Here are some tips for a successful interview:\n1. Research the company and role.\n2. Practice your responses to common questions.\n3. Dress professionally.\n4. Bring copies of your resume.\n5. Prepare questions to ask the interviewer.\nIs there anything else you'd like to know about interviews?"
#                 },
#                 {
#                 "role": "user",
#                 "content": "What should I include in my resume?"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": " In your resume, include your contact information, a summary or objective statement, your work experience, education, skills, and any relevant certifications or awards. Tailor your resume to match the job you're applying for. Would you like more resume-writing tips?\n"
#                 },
#                 {
#                 "role": "user",
#                 "content": "Sorry, I'm unable to understand. Can you elaborate more?"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": " Of course, I'll provide more details."
#                 },
#                 {
#                 "role": "user",
#                 "content": "No, that's enough for now. Thanks, Ayesha!"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": "You're welcome! If you have any more questions in the future or need further assistance with interview preparation, feel free to reach out. Good luck with your interviews!"
#                 },
#                 {
#                 "role": "user",
#                 "content": "how's the weather?"
#                 },
#                 {
#                 "role": "assistant",
#                 "content": "Sorry, I'm unable to understand. Can you elaborate more?"
#                 }
#             ],
#             temperature=1,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0,
#             stop=["/n"]
#         )
#         return jsonify({"message": bot_response})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

@app.route("/api", methods=["POST"])
def chat_with_bot():
    try:
        user_message = request.json["message"]

        # Send user's message to OpenAI API for processing
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                  "role": "system",
                  "content": "You are a helpful assistant"
                },
                {
                    "role": "user",
                    "content": user_message
                },
            ],
            # temperature=1,
            # max_tokens=1000,
            # top_p=1,
            # frequency_penalty=0,
            # presence_penalty=0,
            
        )

        bot_response = response.choices[0].message['content']

        return jsonify({"message": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
