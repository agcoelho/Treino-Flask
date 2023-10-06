from flask_sqlalchemy import SQLAlchemy
from FakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = database.Column(database.Integer, nullable=False, primary_key=True)
    username = database.Column(database.String, nullable=False, unique=True)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship('Foto', backref='Usuario', lazy=True)

class Foto(database.Model):
    __tablename__ = 'fotos'
    id = database.Column(database.Integer, nullable=False, primary_key=True)
    img = database.Column(database.String, nullable=False, default= 'default.png')
    data_postagem = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuarios.id'), nullable=False)



