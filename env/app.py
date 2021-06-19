from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index(): 
    print("respuesta")
    return "<h1>ya casi</h1>"

@app.route('/hello/<name>')
def prueba(name): 
    fecha_actual=datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    
    print("respuesta")
    return fecha_actual

if __name__ == '__main__':
    app.run(port=5000, debug=True)