import logging
from model.Mensagem_model import MensagemModel
from util.messages import (
    resp_error,
    resp_not_found,
    resp_post_ok,
    resp_get_ok,
    resp_ok
)
from service.db_connection import get_table


class MensagemService:

    def __init__(self, table=None):
        if table:
            self.table = table
        else:
            self.table = get_table(MensagemModel)

    def start_db(self):
        self.table.create_table()

    def find(self, params, id=None):
        if id is None:
            logging.info('Consulta lista de mensagens...')
            found = self.table.find_all(
                20,
                self.table.get_conditions(params, False)
            )
        else:
            logging.info(f'Procurando "{id}" nas mensagens ...')
            found = self.table.find_one([id])
        if not found:
            return resp_not_found()
        return resp_get_ok(found)

    def insert(self, json):
        logging.info('Gravando nova mensagem')
        errors = self.table.insert(json)
        if errors:
            return resp_error(errors)
        return resp_post_ok(json)

    def update(self, json):
        logging.info('Alterando uma mensagem ...')
        if 'id' not in json:
            return resp_error('Dados incompletos')
        # --- Só permite alterar a situação da mensagem: ---
        json = {
            'id': json['id'],
            'situacao': json.get('situacao', 1)
        }
        # ---------------------------------------------------
        if not self.table.update(json):
            return resp_error('Falha ao alterar Mensagem.')
        return resp_ok("Registro alterado OK!")

    def delete(self, id):
        logging.info('Removendo uma Mensagem ...')
        self.table.delete(id)
        return resp_ok("Registro excluído OK!")
