import os
from util.tester import Tester
from util.db.lite_table import LiteTable


# ----------------------------------------------
MAGALU_USER = os.environ.get(
    'MAGALU_USER',
    ''
)
MAGALU_PASSWORD = os.environ.get(
    'MAGALU_PASSWORD',
    ''
)
MAGALU_HOST = os.environ.get(
    'MAGALU_HOST',
    'localhost'
)
# ----------------------------------------------


def get_table(schema):
    return LiteTable(schema, {
        # ---- MySql -------------------------
        # "host": MAGALU_HOST,
        # "user": MAGALU_USER,
        # "password": MAGALU_PASSWORD,
        # "database": "magalu"
        # ---- Sqlite -----------------------
        "database": Tester.temp_file()
    })
