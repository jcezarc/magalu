import os
import uuid

def add_record(service):
    record = service.table.default_values()
    return service.insert(record)[1]

class Tester:
    def __init__(self, callback):
        self.callback = callback
    @staticmethod
    def temp_file():
        dst = './tests/temp'
        if not os.path.exists(dst):
            os.makedirs(dst)
        return os.path.join(
            dst, 
            str(uuid.uuid4())+'.db'
        )

    def find_success(self):
        service = self.callback()
        add_record(service)
        status_code = service.find(None, 0)[1]
        assert status_code == 200
    def find_failure(self):
        service = self.callback()
        status_code = service.find(None, 0)[1]
        assert status_code == 404
    def insert_success(self):
        service = self.callback()
        status_code = add_record(service)
        assert status_code == 201
    def insert_failure(self):
        service = self.callback()
        status_code = service.insert({})[1]
        assert status_code == 400
