from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db = SQLAlchemy(app)


class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    elemento = db.Column(db.String(100), nullable=False) 

    def __repr__(self):
        return f'<Elemento {self.elemento}>'


with app.app_context():
    db.create_all()
