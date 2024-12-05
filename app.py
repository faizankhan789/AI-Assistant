from flask import Flask, render_template, request, jsonify
import chatbotlogic  # Import the chatbot logic from chatbotlogic.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the HTML file

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get message from frontend
    response = chatbotlogic.get_response(user_input)  # Get chatbot response
    return jsonify({"response": response})  # Send response back to frontend

if __name__ == '__main__':
    app.run(debug=True)
