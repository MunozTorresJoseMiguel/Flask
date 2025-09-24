from flask import Flask
#para describir rutas es con el @app.router("/")
app = Flask (__name__)

@app.route("/")
def hola_mundo():
    return "<h1> hola mundo desde Flask! <h1>"

@app.route("/otra")
def hola_mundo1():
    return "<h1> hola mundo desde Flask En otra ruta! <h1>"

#name y main guardan el tipo de dato de la app y activa el modo de depuracion

if __name__ == "__main__":
    app.run(debug=True)
#para ejecutar es python app.py y crea un servidor web para ejecutar paginas 

