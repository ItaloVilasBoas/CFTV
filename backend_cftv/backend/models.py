import base64
from . import db

class Fotos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    def to_dict(self):
        return {'id': self.id, 'id_funcionario': self.id_funcionario, 'data': self.data }

class Setor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    cameras = db.Column(db.String, nullable=False)
    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'cameras': [int(camera) for camera in self.cameras.split(',') if camera.isdigit()] }

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=False)
    setores = db.Column(db.String, nullable=False)
    foto = db.Column(db.LargeBinary, nullable=True)
    def to_dict(self):
        return {
            'id': self.id, 
            'nome': self.nome, 
            'setores': [int(setor) for setor in self.setores.split(',') if setor.isdigit()], 
            'foto': base64.b64encode(self.foto).decode('utf-8') if self.foto is not None else None
        }

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True , nullable=False)
    senha = db.Column(db.String, nullable=False)
    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'senha': self.senha }

