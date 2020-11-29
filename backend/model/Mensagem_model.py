from marshmallow import Schema
from marshmallow.fields import Str, Integer, Nested, Date
from Pessoa_model import PessoaModel


class MensagemModel(Schema):
    id = Str(primary_key=True, default="000", required=True)
    data_hora = Date()
    tipo = Str()
    situacao = Integer(default=0)
    assunto = Str()
    conteudo = Str()
    de = Nested(PessoaModel)
    para = Nested(PessoaModel)
