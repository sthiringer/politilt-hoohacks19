from flask import Flask, jsonify, request
from tf.bias_analyzer import BiasAnalyzer
import time
from random import random

app = Flask(__name__)
print('Instantiated flask app. Loading model...')
start_time = time.time()
bias_analyzer = BiasAnalyzer()
elapsed_time = time.time() - start_time
print('Loaded model in ' + time.strftime('%S', time.gmtime(elapsed_time)) + 's. Server up!')
print()

@app.route('/')
def index():
    return 'Welcome to the Slant index. Access the score API by sending a POST to the /score endpoint.'

@app.route('/score', methods=['POST'])
def score():
    data = request.get_json()
    print('received data:', data)
    if not data:
    	print("???")
    	return request_error('no body provided')
    elif 'text' not in data:
			return request_error('must provide text attribute')
    article = data['text']
    score = bias_analyzer.get_article_bias(article)
    return jsonify({ 'score': score })

@app.route('/random_score', methods=['GET', 'POST'])
def random_score():
    sign = -1 if random() < 0.5 else 1
    r = random() * sign
    return jsonify({ 'score': r })


def request_error(error_msg):
	return jsonify({'error': error_msg}), 500
