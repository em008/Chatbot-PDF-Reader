from flask import Flask, render_template, request # Import libraries
import chatbot # Import ML model function module

# Initialize Flask app
app = Flask(__name__)

# Default home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')
    return str(chatbot.CreateChatbot().invoke(user_text))

if __name__ == "__main__":
    app.run()
  
