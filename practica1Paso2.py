from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/')

def hello():

    return 'Bienvenido'