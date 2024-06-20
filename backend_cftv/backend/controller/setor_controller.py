from flask import Response, request, jsonify
from .. import app, db
from ..models import Setor

@app.route('/setor/<id_setor>', methods=['GET'])
def get_setor(id_setor):
    setor = Setor.query.get(id_setor)
    return jsonify(setor.to_dict())

@app.route('/setor', methods=['GET'])
def get_setores():
    setores_json = [setor.to_dict() for setor in Setor.query.all()]
    return jsonify(setores_json)

@app.route('/setor', methods=['POST'])
def post_setor():
    cameras = ','.join([str(n) for n in request.json['cameras']])
    setor = Setor(nome = request.json['nome'], cameras = cameras)
    db.session.add(setor)
    db.session.commit()
    return Response(status=201)

@app.route('/setor/<id_setor>', methods=['PUT'])
def put_setor(id_setor):
    setor = Setor.query.get(setor['id'])
    setor.nome = setor['nome']
    setor.cameras = setor['cameras']
    db.session.commit()
    return Response(status=204)

@app.route('/setor/<id_setor>', methods=['DELETE'])
def delete_setor(id_setor):
    setor = Setor.query.get(setor['id'])
    db.session.delete(setor)
    db.session.commit()
    return Response(status=204)

