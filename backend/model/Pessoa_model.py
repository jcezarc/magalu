from marshmallow import Schema
from marshmallow.fields import Str


PK_DEFAULT_VALUE = "P0"


class PessoaModel(Schema):
    cpf_cnpj = Str(
        primary_key=True,
        default=PK_DEFAULT_VALUE,
        required=True
    )
    nome = Str()
    email = Str()
    celular = Str()
