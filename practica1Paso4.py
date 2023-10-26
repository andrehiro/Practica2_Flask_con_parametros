from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<int:numero>')

def hello(numero):

    return 'Bienvenido'+str(numero)