from flask import Flask, jsonify, request

from random import random

from tf.bias_analyzer import BiasAnalyzer
from debug_bias_analyzer import DebugBiasAnalyzer

app = Flask(__name__)


APP_DEBUG_MODE = True

if APP_DEBUG_MODE:
	bias_analyzer = DebugBiasAnalyzer()
else:
	bias_analyzer = BiasAnalyzer()
	

@app.route('/')
def index():
    return 'Welcome to the Slant index. Access the score API by sending a POST to the /score endpoint.'

@app.route('/score', methods=['POST'])
def get_score():
    data = request.json
    if not data:
        return 'Error: no body in request!', 400
    elif 'text' not in data:
        return 'Error: data needs text attrib', 400
    elif 'source' not in data:
        return 'Error: data needs source attrib', 400
    # Get text from request
    text = data['text']
    src_url = data['source']
    if APP_DEBUG_MODE:
        score = bias_analyzer.score(src_url)
    else:
        score, _ = bias_analyzer.get_article_bias(src_url, text)
    return jsonify({ 'score': score })

@app.route('/random_score', methods=['GET', 'POST'])
def get_random_score():
    return jsonify({ 'score': debug_bias_analyzer.random_score() })

if __name__ == "__main__":
    app.run(host='0.0.0.0')