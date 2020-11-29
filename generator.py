'''
Gera os testes funcionais:
Faz requisições à API e compara
 os resultados em cada situação
'''

import random
import requests
from faker import Faker


BASE_URL = 'http://localhost:5000/magalu/comunica/{}'
P1 = 0
P2 = 1
P3 = 2
TIPOS_MSG = ['email', 'sms', 'whatsapp', 'push']
SITUACAO_ENVIADO = 1
SITUACAO_NAO_ENV = 0


class Generator:

    def __init__(self, faker):
        self.faker = faker
        self.pessoas = []

    def cria_pessoa(self, id):
        record = {}
        fake = self.faker
        print('-'*100)
        print(f'Criando {id}...')
        record['cpf_cnpj'] = fake.cpf()
        record['nome'] = fake.name()
        record['celular'] = fake.phone_number()
        record['email'] = fake.email()
        url = BASE_URL.format('Pessoa')
        resp = requests.post(url, record)
        self.pessoas.append(record['cpf_cnpj'])
        assert resp.status_code == 201

    def cria_mensagem(self, id, de, para):
        record = {}
        fake = self.faker
        print('-'*100)
        print(f'Criando {id}...')
        conteudo = fake.text()
        record['id'] = id
        record['data_hora'] = fake.date()
        record['tipo'] = random.choice(TIPOS_MSG)
        record['situacao'] = SITUACAO_NAO_ENV
        record['assunto'] = id
        record['conteudo'] = conteudo
        record['de'] = self.pessoas[de]
        record['para'] = self.pessoas[para]
        url = BASE_URL.format('Mensagem')
        resp = requests.post(url, record)
        assert resp.status_code == 201

    def consulta_msg(self, params):

        def existe_mensagem(id, dados):
            for item in dados:
                if item['id'] == id:
                    return True
            return False
        url = BASE_URL.format('Mensagem') + '?'
        esperado = params.pop('esperado')
        args_query = []
        for key, value in params.items():
            args_query.append('{}={}'.format(
                key,
                value
            ))
        url += '&'.join(args_query)
        resp = requests.get(url)
        assert resp.status_code == 200
        dados = resp.json()
        assert len(dados) == len(esperado)
        for id in esperado:
            assert existe_mensagem(id, dados)

    def run(self):
        self.cria_pessoa('P1')
        self.cria_pessoa('P2')
        self.cria_mensagem('M1', P1, P2)
        self.cria_pessoa('P3')
        self.cria_mensagem('M2', P2, P3)
        self.cria_mensagem('M3', P1, P3)
        self.cria_mensagem('M4', P3, P1)
        self.consulta_msg({
            'de': P1,
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M1', 'M3']
        })
        self.consulta_msg({
            'para': P3,
            'situacao': SITUACAO_NAO_ENV,
            'esperado': ['M2', 'M3']
        })
        print('='*100)
        print('>> Teste concluído com sucesso!!!\n\n')


if __name__ == '__main__':
    generator = Generator(
        Faker('pt_BR')
    )
    generator.run()
