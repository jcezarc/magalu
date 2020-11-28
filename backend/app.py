# -*- coding: utf-8 -*-
"""
API de comunicação do Magalu
"""

import logging
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from util.swagger_generator import FlaskSwaggerGenerator
from model.Pessoa_model import PessoaModel
from resource.Pessoa_by_id import PessoaById
from resource.all_Pessoa import AllPessoa
from model.Mensagem_model import MensagemModel
from resource.Mensagem_by_id import MensagemById
from resource.all_Mensagem import AllMensagem


BASE_PATH = '/magalu/comunica'


def config_routes(app):
    api = Api(app)
    # --- Resources: ----
    api.add_resource(
        PessoaById,
        f'{BASE_PATH}/Pessoa/<cpf_cnpj>',
        methods=['GET'],
        endpoint='get_Pessoa_by_id'
    )
    api.add_resource(
        AllPessoa,
        f'{BASE_PATH}/Pessoa',
        methods=['GET'],
        endpoint='get_AllPessoa'
    )
    api.add_resource(
        AllPessoa,
        f'{BASE_PATH}/Pessoa',
        methods=['POST'],
        endpoint='post_Pessoa'
    )
    api.add_resource(
        AllPessoa,
        f'{BASE_PATH}/Pessoa',
        methods=['PUT'],
        endpoint='put_Pessoa'
    )
    api.add_resource(
        PessoaById,
        f'{BASE_PATH}/Pessoa/<cpf_cnpj>',
        methods=['DELETE'],
        endpoint='delete_Pessoa'
    )
    api.add_resource(
        MensagemById,
        f'{BASE_PATH}/Mensagem/<id>',
        methods=['GET'],
        endpoint='get_Mensagem_by_id'
    )
    api.add_resource(
        AllMensagem,
        f'{BASE_PATH}/Mensagem',
        methods=['GET'],
        endpoint='get_AllMensagem'
    )
    api.add_resource(
        AllMensagem,
        f'{BASE_PATH}/Mensagem',
        methods=['POST'],
        endpoint='post_Mensagem'
    )
    api.add_resource(
        AllMensagem,
        f'{BASE_PATH}/Mensagem',
        methods=['PUT'],
        endpoint='put_Mensagem'
    )
    api.add_resource(
        MensagemById,
        f'{BASE_PATH}/Mensagem/<id>',
        methods=['DELETE'],
        endpoint='delete_Mensagem'
    )
    # -------------------


def set_swagger(app):
    swagger_url = '/docs'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_url,
        '/api',
        config={
            'app_name': "*- Comunicações do Magalu -*"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)


def swagger_details(args):
    id_route = args[0]
    params = args[1]
    model = None
    resource = None
    docstring = ""
    if id_route == 'docs':
        docstring = """Documentação Swagger
        #Doc
        """
    elif id_route == 'Pessoa':
        if not params:
            resource = AllPessoa
        else:
            resource = PessoaById
        model = PessoaModel()
    elif id_route == 'Mensagem':
        if not params:
            resource = AllMensagem
        else:
            resource = MensagemById
        model = MensagemModel()
    ignore = False
    return model, resource, docstring, ignore


logging.basicConfig(
    filename='magalu.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

APP = Flask(__name__)
CORS(APP)

config_routes(APP)
set_swagger(APP)


@APP.route('/api')
def get_api():
    """
    API json data

    #Doc
    """
    generator = FlaskSwaggerGenerator(
        swagger_details,
        None
    )
    return jsonify(generator.content)


if __name__ == '__main__':
    APP.run(debug=True)
