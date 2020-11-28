import json
from flask_restful import Resource
from flask import request
from service.Mensagem_service import MensagemService


class AllMensagem(Resource):

    def get(self):
        """
        Retorna uma lista de mensagens

        #Consulta
        """
        service = MensagemService()
        return service.find(request.args)

    def post(self):
        """
        Grava um novo registro de Mensagem

        #Gravação
        """
        req_data = request.get_json()
        service = MensagemService()
        return service.insert(req_data)

    def put(self):
        """
        Atualiza os dados de uma mensagem

        #Gravação
        """
        req_data = json.loads(request.data.decode("utf8"))
        service = MensagemService()
        return service.update(req_data)
