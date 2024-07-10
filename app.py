from flask import Flask, request, jsonify
from flask_cors import CORS
from meta_ai_api import MetaAI
import os 

app = Flask(__name__)
CORS(app) # <-- Enable CORS for all routes

ai = MetaAI()

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to my chatbot API!'

@app.route('/endpoint', methods=['POST'])
def handle_chatbot_request():
    message = request.json['message']
    response = ai.prompt(message)
    return jsonify({'response': response})

#if __name__ == '__main__':
 #    app.run(debug=True)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
 app.listen(process.env.PORT || 5000)
