from flask import Flask
from flask import request
from requests import codes
from time import time_ns
from os import walk
from json import dumps, loads
app = Flask(__name__)
headers = {'Content-Type': 'application/json'}


@app.route('/', methods=['GET'])
@app.route('/health-check', methods=['GET'])
def default_page():
    message = {
        'status': 'Flask up!'
    }
    return app.make_response((dumps(message), codes.ok, headers))


if __name__ == '__main__':
    app.run(host='192.168.1.100', port='5000', debug=True)
