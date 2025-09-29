#Siempre importar la libreria de flask from flask import Flask 
from flask import Flask
#para describir rutas es con el @app.router("/")
app = Flask (__name__)
#Esto nos crea nuestro servider


@app.route("/")
def hola_mundo():
    return '''
<h1> Bienvenidos ala calculadora de Python! <h1>
<h3>para sumar  teclear o escribe en el navegador 127.0.0.1:5000/sumar/10/20</h3>
<h3>para restar teclear o escribe en el navegador 127.0.0.1:5000/restar/10/20</h3>
<h3>para obtener el valor maximo  teclear o escribe en el navegador 127.0.0.1:5000/maximo/10/20</h3>
'''
@app.route("/sumar/<int:num1>/<int:num2>")
def sumar(valor_uno,valor_dos):
    resultado = valor_uno + valor_dos
    return f'''
<h1> El resultado de la suma es: {resultado} <h1>
'''
@app.route("/restar/<int:num1>/<int:num2>")
def restar(num1,num2):
    resultado = num1 - num2
    return f'''
<h1> El resultado de la resta es: {resultado} <h1>
'''
@app.route("/maximo/<int:num1>/<int:num2>")
def maximo(num1,num2):
    if num1 > num2:
        resultado = num1
    else:
        resultado = num2
    return f'''
<h1> El numero maximo es: {resultado} <h1>
'''
if __name__ == "__main__":
    app.run(debug=True)




#bien venidoa las calculadora de python
#para sumar  teclear o escribe en el navegador 127.0.0.1:5000/sumar/10/20
#para restar teclear o escribe en el navegador 127.0.0.1:5000/restar/10/20
#para obtener el valor maximo  teclear o escribe en el navegador 127.0.0.1:5000/maximo/10/20