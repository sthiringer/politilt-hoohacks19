from flask import Flask, jsonify, request

from random import random

from tf.bias_analyzer import BiasAnalyzer

app = Flask(__name__)
bias_analyzer = BiasAnalyzer()

@app.route('/')
def index():
    return 'Welcome to the Slant index. Access the score API by sending a POST to the /score endpoint.'

@app.route('/score', methods=['POST'])
def get_score():
    data = request.json
    if not data:
        return 'Error: no body in request!'
    elif 'text' not in data:
        return 'Error: data needs text attrib'
    elif 'source' not in data:
        return 'Error: data needs source attrib'
    # Get text from request
    text = data['text']
    src_url = data['source']
    score, _ = bias_analyzer.get_article_bias(src_url, text)
    return jsonify({ 'score': score })

@app.route('/random_score', methods=['GET', 'POST'])
def get_random_score():
    return jsonify({ 'score': random_score() })

def random_score():
    sign = -1 if random() < 0.5 else 1
    return random() * sign

if __name__ == "__main__":
    app.run(host='0.0.0.0')