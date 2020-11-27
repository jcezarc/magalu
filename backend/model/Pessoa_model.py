from marshmallow import Schema
from marshmallow.fields import Str, Nested, List, Integer, Float, Date, Boolean


class PessoaModel(Schema):
    cpf_cnpj = Str(primary_key=True, default="000", required=True)
    nome = Str()
    email = Str()
    celular = Str()
