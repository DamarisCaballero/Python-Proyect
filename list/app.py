from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

titulares = [
    # Lista de titulares de noticias
    "Aumenta la demanda de energías renovables",
    "Desarrollan vacuna efectiva contra el virus del dengue",
    # ... (agrega los demás titulares de noticias)
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        palabra_clave = request.form['palabra_clave']
        return redirect(url_for('resultados', palabra_clave=palabra_clave))
    return render_template('home.html')

@app.route('/resultados')
def resultados():
    palabra_clave = request.args.get('palabra_clave')
    titulares_filtrados = [titular for titular in titulares if palabra_clave.lower() in titular.lower()]
    return render_template('resultados.html', titulares=titulares_filtrados, palabra_clave=palabra_clave)

if __name__ == '__main__':
    app.run()
