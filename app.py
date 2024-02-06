from flask import Flask, render_template, request, jsonify # Import libraries
import chatbot # Import ML model function module

# Initialize Flask app
app = Flask(__name__)

# Initialize chatbot
def get_chatbot_response(user_input):
    # chatbot logic goes here
    return "Chatbot response"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    chatbot_response = get_chatbot_response(user_input)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
  
