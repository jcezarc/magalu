import json
from flask_restful import Resource
from flask import request, jsonify

from service.Pessoa_service import PessoaService

class AllPessoa(Resource):

    
    def get(self):
        """
        Retorna uma lista de pessoas

        #Consulta
        """
        service = PessoaService()
        return service.find(request.args)
    
    
    def post(self):
        """
        Grava um novo registro de Pessoa

        #Gravação
        """
        req_data = request.get_json()
        service = PessoaService()
        return service.insert(req_data)

    
    def put(self):
        """
        Atualiza um registro de pessoa.

        #Gravação
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = PessoaService()
        return service.update(req_data)
