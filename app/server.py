from flask import Flask, render_template, request
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return main.chat(userText)

host = '192.168.0.187'
port = 8080
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)