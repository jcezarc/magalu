from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean
from model.Pessoa_model import PessoaModel
from model.Pessoa_model import PessoaModel


class MensagemModel(Schema):
    id = Str(primary_key=True, default="000", required=True)
    data_hora = Date()
    tipo = Str()
    situacao = Str()
    assunto = Str()
    conteudo = Str()
    de = Nested(PessoaModel)
    para = Nested(PessoaModel)
