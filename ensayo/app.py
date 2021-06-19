from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(): 
    print("respuesta")
    return "<h1>Este es otro ensayo</h1>"

