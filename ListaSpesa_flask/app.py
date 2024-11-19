from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


lista_spesa = []

@app.route('/')
def index():

    return render_template('index.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():

    elemento = request.form.get('elemento')
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('index'))

@app.route('/rimuovi/<int:indice>')
def rimuovi(indice):

    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('index'))

@app.route('/svuota')
def svuota():

    lista_spesa.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
