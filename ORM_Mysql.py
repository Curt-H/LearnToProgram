import pymysql
import password


class SQLModel(object):
    db_name = 'test998707'
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=password.password,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    def __init__(self, form):
        self.id = form['id']
        self.name = form['name']
        self.price = form['price']

    @classmethod
    def table_name(cls):
        return f'`{cls.__name__}`'

    @classmethod
    def insert(cls, form):
        sql_keys = ', '.join([f'`{k}`' for k in form.keys()])
        sql_values = ', '.join([f'`{v}`' for v in form.values()])

