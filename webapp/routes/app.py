
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/your_endpoint', methods=['POST'])
def handle_post_request():
    data = request.json
    # Process the data and return a response
    response = {'message': 'POST request received', 'data': data}
    return response, 200
