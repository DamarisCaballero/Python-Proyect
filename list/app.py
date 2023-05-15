from flask import Flask, render_template, request

app = Flask(__name__)

titulares = [
    "Aumenta la demanda de energías renovables",
    "Desarrollan vacuna efectiva contra el virus del dengue",
    "El mercado de criptomonedas experimenta volatilidad",
    "Descubren nueva especie de dinosaurio en América",
    "Avanza la investigación para la cura del Alzheimer",
    "Lanzamiento exitoso del satélite espacial comercial",
    "Nuevas regulaciones para proteger el medio ambiente",
    "Inauguración de un parque dedicado a la historia local",
    "Las ventas de carros eléctricos alcanzan cifras récord",
    "Investigadores descubren evidencias de vida en Marte",
    "Crece la preocupación por el calentamiento global",
    "Se detecta una nueva variante de virus informático",
    "Declaran emergencia sanitaria por brote de enfermedad",
    "Desarrollan tecnología para la generación de energía limpia",
    "Celebrities se unen para luchar contra el hambre en el mundo",
    "Avances en la inteligencia artificial transforman la industria",
    "Nuevo récord de producción de alimentos orgánicos",
    "Descubren posible cura para la diabetes tipo 2",
    "Conferencia aborda el futuro de la exploración espacial",
    "Invertir en bienes raíces: una opción segura",
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        palabra_clave = request.form['palabra_clave']
        return redirect('/resultados?palabra_clave=' + palabra_clave)
    return render_template('home.html')

@app.route('/resultados')
def resultados():
    palabra_clave = request.args.get('palabra_clave', '')
    titulares_filtrados = [titular for titular in titulares if palabra_clave.lower() in titular.lower()]
    return render_template('resultados.html', titulares=titulares_filtrados, palabra_clave=palabra_clave)

if __name__ == '__main__':
    app.run()
