from flask import Flask, render_template, request, jsonify
from meta_ai_api import MetaAI
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

ai = MetaAI()

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint
@app.route('/endpoint', methods=['POST'])
def handle_chatbot_request():
    message = request.json['message']
    logging.debug(f"Received message: {message}")
    try:
        response = ai.prompt(message)
        logging.debug(f"Meta AI response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        logging.error(f"Error handling request: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
