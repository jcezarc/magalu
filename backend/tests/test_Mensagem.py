from service.Mensagem_service import MensagemService
from model.Mensagem_model import MensagemModel, PK_DEFAULT_VALUE
from util.db.lite_table import LiteTable
from util.tester import Tester


def get_service():
    table = LiteTable(
        MensagemModel, {
            'database': Tester.temp_file()
            #  'database': ':memory:'
        }
    )
    table.create_table()
    return MensagemService(table)


def test_find_success():
    test = Tester(get_service)
    test.find_success()


def test_find_failure():
    test = Tester(get_service)
    test.find_failure()


def test_insert_success():
    test = Tester(get_service)
    test.insert_success()


def test_insert_failure():
    test = Tester(get_service)
    test.insert_failure()


def test_update_failure():
    test = Tester(get_service)
    test.update_failure()


def test_update_success():
    test = Tester(get_service)
    test.update_success({
        'id': PK_DEFAULT_VALUE,
        'situacao': 3
    })
