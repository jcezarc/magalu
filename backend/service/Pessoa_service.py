import logging
from model.Pessoa_model import PessoaModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table


class PessoaService:
    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(PessoaModel)

    def find(self, params, cpf_cnpj=None):
        if cpf_cnpj is None:
            logging.info('Consultando lista de pessoas...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        else:
            logging.info(f'Procurando "{cpf_cnpj}" em pessoas ...')
            found = self.table.find_one([cpf_cnpj])
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('Novo registro gravado em Pessoa.')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok(json)

    def update(self, json):
        logging.info('Alterando uma Pessoa ...')
        if not self.table.update(json):
            return resp_error('Falha ao alterar Pessoa.')
        return resp_ok("Gravado OK!")

    def delete(self, cpf_cnpj):
        logging.info('Removendo uma Pessoa ...')
        self.table.delete(cpf_cnpj)
        return resp_ok("Registro excluído OK!")
