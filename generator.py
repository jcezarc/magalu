'''
Gera os testes funcionais:
Faz requisições à API e compara
 os resultados em cada situação
'''

import random
import requests
from faker import Faker


BASE_URL = 'http://localhost:5000/magalu/comunica/{}'
TIPOS_MSG = ['email', 'sms', 'whatsapp', 'push']
SITUACAO_ENVIADA = 1
SITUACAO_NAO_ENV = 0


class Generator:

    def __init__(self, faker):
        self.faker = faker

    def cria_pessoa(self, id):
        record = {}
        fake = self.faker
        print('-'*50)
        print('[POST]', id)
        record['cpf_cnpj'] = id
        record['nome'] = fake.name()
        record['celular'] = fake.phone_number()
        record['email'] = fake.email()
        url = BASE_URL.format('Pessoa')
        resp = requests.post(url, json=record)
        assert resp.status_code == 201

    def cria_mensagem(self, id, de, para):
        record = {}
        fake = self.faker
        print('-'*50)
        print('[POST]', id)
        conteudo = fake.text()
        record['id'] = id
        record['data_hora'] = fake.date()
        record['tipo'] = random.choice(TIPOS_MSG)
        record['situacao'] = SITUACAO_NAO_ENV
        record['assunto'] = id
        record['conteudo'] = conteudo
        record['de'] = de
        record['para'] = para
        url = BASE_URL.format('Mensagem')
        resp = requests.post(url, json=record)
        assert resp.status_code == 201

    def consulta_msg(self, params):

        def existe_mensagem(id, dados):
            for item in dados:
                if item['id'] == id:
                    return True
            return False
        url = BASE_URL.format('Mensagem')
        esperado = params.pop('esperado')
        args_query = []
        for key, value in params.items():
            args_query.append('{}={}'.format(
                key,
                value
            ))
        if args_query:
            url += '?'
        url += '&'.join(args_query)
        print('-'*50)
        print('[GET]', url)
        resp = requests.get(url)
        if not esperado:
            assert resp.status_code == 404
            return
        assert resp.status_code == 200
        dados = resp.json()['data']
        assert len(dados) == len(esperado)
        for id in esperado:
            assert existe_mensagem(id, dados)

    def altera_situacao(self, id, situacao):
        record = {}
        record['id'] = id
        record['sitacao'] = situacao
        print('-'*50)
        print('[PUT]', id, situacao)
        url = BASE_URL.format('Mensagem')
        resp = requests.put(url, json=record)
        assert resp.status_code == 200

    def exclui_msg(self, id):
        url = BASE_URL.format('Mensagem')
        url += f'/{id}'
        print('-'*50)
        print('[DELETE]', url)
        resp = requests.delete(url)
        assert resp.status_code == 200

    def run(self):
        # 1
        self.cria_pessoa('P1')
        # 2
        self.cria_pessoa('P2')
        # 3
        self.cria_mensagem('M1', 'P1', 'P2')
        # 4
        self.cria_pessoa('P3')
        # 5
        self.cria_mensagem('M2', 'P2', 'P3')
        # 6
        self.cria_mensagem('M3', 'P1', 'P3')
        # 7
        self.cria_mensagem('M4', 'P3', 'P1')
        # 8
        self.consulta_msg({
            'de': 'P1',
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M1', 'M3']
        })
        # 9
        self.consulta_msg({
            'para': 'P3',
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M2', 'M3']
        })
        # 10
        self.altera_situacao('M1', SITUACAO_ENVIADA)
        # 11
        self.consulta_msg({
            'de': 'p1',
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M3']
        })
        # 12
        self.altera_situacao('M3', SITUACAO_ENVIADA)
        # 13
        self.consulta_msg({
            'para': 'P3',
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M2']
        })
        # 14
        self.consulta_msg({
            'de': 'P1',
            'situacao': SITUACAO_NAO_ENV,
            'esperado': []
        })
        # 15
        self.consulta_msg({
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M2', 'M4']
        })
        # 16
        self.consulta_msg({
            'situacao': SITUACAO_ENVIADA,
            'esperado': ['M1', 'M3']
        })
        # 17
        self.exclui_msg('M3')
        # 18
        self.consulta_msg({
            'esperado': ['M1', 'M2', 'M4']
        })
        # 19
        self.consulta_msg({
            'situacao': SITUACAO_ENVIADA,
            'esperado': ['M1']
        })
        # 20
        self.exclui_msg('M2')
        # 21
        self.consulta_msg({
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M4']
        })
        # 18
        self.consulta_msg({
            'esperado': ['M1', 'M4']
        })
        print('='*50)
        print('>> Teste concluído com sucesso!!!\n\n')


if __name__ == '__main__':
    generator = Generator(
        Faker('pt_BR')
    )
    generator.run()
