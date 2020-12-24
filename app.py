from flask import Flask, request, redirect, url_for, render_template
from requests import codes
from time import time_ns
from os import walk
from json import dumps, loads
app = Flask(__name__)
headers = {'Content-Type': 'application/json'}


@app.route('/', methods=['GET']) 
def home():
    return render_template('index.html')

@app.route('/health-check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return app.make_response((dumps(message), codes.ok, headers))


@app.route('/subscribe', methods=['GET'])
def subscription():
  return render_template('subscribe_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
