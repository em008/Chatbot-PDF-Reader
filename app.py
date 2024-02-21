from flask import Flask, request, render_template, jsonify  # Import libraries
import chatbot  # Import functions file
import os

# Initialize Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse JSON data
        user_input = request.json['message']

        # Check for exit commands
        if user_input.lower() in ["exit", "quit", "bye"]:
            response = {"response": "Goodbye!"}
            return jsonify({'response': response['response']})
        else:
            response = chatbot_input.invoke(user_input)

        # Return response as JSON
        return jsonify({'query': response['query'], 'response': response['result']})

    except KeyError as e:
        # KeyError occurs when the 'message' key is missing in the JSON data
        error_message = "Request body must include 'message' field: {}".format(str(e))
        response = {"response": error_message}
        return jsonify({'response': response['response']}), 400

    except Exception as e:
        # Catching other unexpected exceptions
        error_message = "Error processing request: {}".format(str(e))
        response = {"response": error_message}
        return jsonify({'response': response['response']}), 400


if __name__ == '__main__':
    huggingface_api_token = chatbot.get_huggingface_api_token()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_api_token

    language_model = chatbot.initialize_language_model()
    pdf_file = chatbot.load_pdf_file()
    chatbot_input = chatbot.create_chatbot(language_model, pdf_file)

    app.run()
