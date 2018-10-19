from flask import Flask, request, jsonify, make_response
from module import methods

use = methods()

app = Flask(__name__)

@app.route('/')
def index():
    return ('Welcome to the API')

@app.route('/data')
def data():
    cort = use.get()
    return jsonify({'data':cort})

@app.route('/post', methods=['POST'])
def poster():
    poster = use.post_data()
    return poster


if __name__=='__main__':
    app.run(debug=True, port=7887)
