

from flask import Flask, render_template, request, redirect, url_for
from models import db, ListaSpesa

@app.route('/')
def home():

    elementi = ListaSpesa.query.all()
    return render_template('index.html', elementi=elementi)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    if request.method == 'POST':
        elemento = request.form['elemento']  
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento)
        db.session.commit()
        return redirect(url_for('home')) 

@app.route('/rimuovi/<int:id>', methods=['GET'])
def rimuovi(id):
    elemento = ListaSpesa.query.get(id)
    db.session.delete(elemento)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/svuota', methods=['GET'])
def svuota():
    ListaSpesa.query.delete() 
    db.session.commit()
    return redirect(url_for('home')) 
