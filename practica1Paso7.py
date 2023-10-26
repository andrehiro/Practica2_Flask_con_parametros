from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/<name>/<int:ncontrol>')

def hello(name,ncontrol):

    return 'Bienvenido '+ name +f" El numero recibido es: {ncontrol}"