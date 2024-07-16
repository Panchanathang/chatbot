from flask import Flask, render_template, request, jsonify
from meta_ai_api import MetaAI
from flask_cors import CORS
import logging
from main import MetaAI
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


ai = MetaAI()

logging.basicConfig(level=logging.DEBUG)


# Serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint
@app.route('/endpoint', methods=['POST'])
def handle_chatbot_request():
    message = request.json['message']
    response = ai.prompt(message)
    return jsonify({'response': response})


if __name__ == '__main__':
 #    app.run(debug=True)

#if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
