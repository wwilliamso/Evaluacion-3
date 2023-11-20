from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/calcular_promedio', methods=['POST'])
def calcular_promedio():
    nota1 = int(request.form['nota1'])
    nota2 = int(request.form['nota2'])
    nota3 = int(request.form['nota3'])
    asistencia = int(request.form['asistencia'])

    promedio = (nota1 + nota2 + nota3) / 3
    aprobado = promedio >= 40 and asistencia >= 75

    return render_template('resultado.html', promedio=promedio, aprobado=aprobado)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

def calcular_nombre_mas_largo_interno(nombre1, nombre2, nombre3):
    nombres = [nombre1, nombre2, nombre3]

    nombre_mas_largo = max(nombres, key=len)
    cantidad_caracteres = len(nombre_mas_largo)

    return nombre_mas_largo, cantidad_caracteres

@app.route('/calcular_nombre_mas_largo', methods=['POST'])
def calcular_nombre_mas_largo():
    # Obtener los nombres del formulario
    nombre1 = request.form['nombre1']
    nombre2 = request.form['nombre2']
    nombre3 = request.form['nombre3']

    nombre_mas_largo, cantidad_caracteres = calcular_nombre_mas_largo_interno(nombre1, nombre2, nombre3)

    return render_template('resultado_nombre_mas_largo.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)