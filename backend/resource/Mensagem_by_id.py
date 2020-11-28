from flask_restful import Resource
from service.Mensagem_service import MensagemService


class MensagemById(Resource):

    def get(self, id):
        """
        Procura uma mensagem pelo <id>

        #Consulta
        """
        service = MensagemService()
        return service.find(None, id)

    def delete(self, id):
        """
        Exclui uma mensagem

        #Gravação
        """
        service = MensagemService()
        return service.delete([id])
