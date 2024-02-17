from flask import Flask, request, render_template, jsonify # Import libraries
import chatbot # Import functions file
from werkzeug.exceptions import BadRequest
import os

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
    except KeyError:
        raise BadRequest('Request body must be JSON and include "message" field')

    if user_input.lower() in ["exit", "quit", "bye"]:
        response = "Goodbye!"
    else:
        response = chatbot_input.invoke(user_input)

    return jsonify({'response': response})

if __name__ == '__main__':
    huggingface_api_token = chatbot.get_huggingface_api_token()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_token

    language_model = chatbot.initialize_language_model()
    pdf_file = chatbot.load_pdf_file()
    chatbot_input = chatbot.create_chatbot(language_model, pdf_file)

    app.run(host='0.0.0.0', port=5000)

