from json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Funcionario):
            return {'id': obj.id, 'nome': obj.nome, 'setores': obj.setores, 'foto': obj.foto}
        if isinstance(obj, Fotos):
            return {'id': obj.id, 'id_funcionario': obj.id_funcionario, 'data': obj.data}
        if isinstance(obj, Setor):
            return obj.to_dict()
        if isinstance(obj, Usuario):
            return {'id': obj.id, 'username': obj.username, 'email': obj.email, 'senha': obj.senha}
        return super(CustomJSONEncoder, self).default(obj)


