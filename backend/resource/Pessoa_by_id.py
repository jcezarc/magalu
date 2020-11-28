from flask_restful import Resource
from service.Pessoa_service import PessoaService


class PessoaById(Resource):

    def get(self, cpf_cnpj):
        """
        Procura uma pessoa pelo cpf_cnpj

        #Consulta
        """
        service = PessoaService()
        return service.find(None, cpf_cnpj)

    def delete(self, cpf_cnpj):
        """
        Exclui uma Pessoa

        #Gravação
        """
        service = PessoaService()
        return service.delete([cpf_cnpj])
