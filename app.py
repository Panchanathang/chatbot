from flask import Flask, render_template, request, jsonify
from meta_ai_api import MetaAI

app = Flask(__name__)

# Serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint
@app.route('/endpoint', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    # Assuming MetaAI class has a method to get a reply
    bot_reply = MetaAI().get_reply(user_message)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
