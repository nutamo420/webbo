
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Ajarn Sun!'

@app.route('/lala')
def lala():
    return 'Lala'

@app.route('/lala/lovesong')
def lalalovesong():
    return 'Lalalovesong'

