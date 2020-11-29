from marshmallow import Schema
from marshmallow.fields import Str, Integer, Nested, Date
from datetime import datetime
from model.Pessoa_model import PessoaModel


def is_valid_date(value):
    today = datetime.today()
    return value >= today.date()


class MensagemModel(Schema):
    id = Str(primary_key=True, default="000", required=True)
    data_hora = Date(validate=is_valid_date)
    tipo = Str()
    situacao = Integer(default=0)
    assunto = Str()
    conteudo = Str()
    de = Nested(PessoaModel)
    para = Nested(PessoaModel)
