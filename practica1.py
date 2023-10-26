from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<name>')

def hello(name):

    return 'Bienvenido'+name