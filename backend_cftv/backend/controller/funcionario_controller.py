from flask import Response, request, jsonify
from flask_cors import cross_origin
from .. import app, db
from ..models import Funcionario, Fotos

def get_foto_by_funcionario_id(id_funcionario):
    return Fotos.query.filter(Fotos.id_funcionario == id_funcionario).all()[0].data

@app.route('/funcionario/<id_funcionario>', methods=['GET'])
def get_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    return jsonify(funcionario.to_dict())

@app.route('/funcionario')
def get_funcionarios():
    funcionarios_json = [funcionario.to_dict() for funcionario in Funcionario.query.all()]
    return jsonify(funcionarios_json)

@app.route('/funcionario', methods=['POST'])
def post_funcionarios():
    setores = ','.join([str(n) for n in request.json['setores']])
    funcionario = Funcionario(nome=request.json['nome'], setores=setores)
    db.session.add(funcionario)
    db.session.commit()
    return jsonify({'id': funcionario.id}), 201

@app.route('/funcionario/<id_funcionario>', methods=['PUT'])
def put_funcionarios(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    if 'nome' in request.json:
        funcionario.nome = request.json['nome']
    if 'setores' in request.json:
        funcionario.setores = ','.join([str(n) for n in request.json['setores']])
    db.session.commit()
    return Response(status=204)

@app.route('/funcionario/<id_funcionario>', methods=['DELETE'])
def delete_funcionarios(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    db.session.delete(funcionario)
    db.session.commit()
    return Response(status=204)

@app.route('/funcionario/<id_funcionario>/foto', methods=['PUT'])
@cross_origin(origins='*')
def atualizar_foto_funcionario(id_funcionario):
    funcionario = Funcionario.query.get(id_funcionario)
    funcionario.foto = get_foto_by_funcionario_id(id_funcionario)
    db.session.commit()
    return Response(status=204)

