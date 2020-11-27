import datetime
import logging

def default_resp(msg, status_code):
    return {
        "timeStamp": str(datetime.datetime.now()),
        "msg": msg
    }

def resp_ok(msg="OK", data=None, status_code=200):
    result = default_resp(msg, status_code)
    if data:
        result['data'] = data
    logging.info(msg)
    return result, status_code

def resp_error(msg, status_code=400):
    result = default_resp(msg, status_code)
    logging.error(f'Erro {status_code}: {msg}')
    return result, status_code

def resp_not_found():
    return resp_error("Nenhum registro encontrado", 404)

def resp_get_ok(data=None):
    return resp_ok('GET ok!', data)

def resp_post_ok(data=None):
    return resp_ok('POST ok!', data, 201)
