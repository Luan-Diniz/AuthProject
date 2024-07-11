import flask_cors, requests
from os import getcwd
from flask import Flask

HOST = '0.0.0.0'
# Check if it is running in Docker.
if getcwd() != '/api':
    HOST = '127.0.0.1'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

app.run(host=HOST)


