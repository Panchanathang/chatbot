from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from meta_ai_api import MetaAI
import os 

app = Flask(__name__)
CORS(app) # <-- Enable CORS for all routes

ai = MetaAI()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def handle_chatbot_request():
    message = request.json['message']
    try:
        response = ai.prompt(message)
        print(f"API Response: {response}")
        return jsonify({'response': response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Failed to obtain a response from Meta AI'})
if __name__ == '__main__':
     app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
