from flask import Flask, jsonify, request

from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Slant index. Access the score API by sending a POST to the /score endpoint.'

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    print('received data:', data)
    return jsonify({ 'score': random_score() })

def random_score():
	sign = -1 if random() < 0.5 else 1
	return random() * sign

if __name__ == "__main__":
    print('runningn adhoc')
    app.run(host='0.0.0.0')
