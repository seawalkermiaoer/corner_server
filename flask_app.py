
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! with HF'

@app.route('/wx')
def hello_wx():
    return 'Hello from Flask! with WX'
