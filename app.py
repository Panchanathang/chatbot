from flask import Flask, render_template, request, jsonify
from meta_ai_api import MetaAI


app = Flask(__name__)



ai = MetaAI()


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
     app.run(debug=True)
