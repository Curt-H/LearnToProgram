import pymysql
import password
import json

from util import log


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

    sql_create = '''
    CREATE TABLE `price` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(45) NOT NULL,
        `madeIn` VARCHAR(45) NOT NULL,
        `price` INT NOT NULL,
        PRIMARY KEY (`id`)
    )'''

    def __init__(self, form):
        self.id = form['id']
        self.name = form['name']
        self.price = form['price']

    @classmethod
    def table_name(cls):
        return 'price'

    @classmethod
    def insert(cls, form):
        sql_keys = ', '.join([f'`{k}`' for k in form.keys()])
        sql_values = ', '.join(['%s'] * len(form))
        sql_insert = f'INSERT INTO {cls.table_name()} ({sql_keys}) VALUES ({sql_values})'

        log(sql_insert)
        values = tuple(form.values())

        with cls.connection.cursor() as cursor:
            cursor.execute(sql_insert, values)
            _id = cursor.lastrowid
        cls.connection.commit()

        return _id

    @classmethod
    def new(cls, form):
        cls_id = cls.insert(form)
        form['id'] = cls_id
        m = cls(form)
        return m

    @classmethod
    def delete(cls, model_id):
        sql_delete = f'DELETE FOROM {cls.table_name()} WHERE `id`=%s'
        log(sql_delete)

        with cls.connection.cursor() as cursor:
            cursor.execute(sql_delete, (model_id,))
        cls.connection.commit()

    @classmethod
    def update(cls, model_id, **kwargs):
        sql_set = ', '.join(
            [f'`{k}`=%s' for k in kwargs.keys()]
        )

        sql_update = f'UPDATE {cls.table_name()} SET {sql_set} WHERE `id`=%s'
        log(sql_update)

        values = list(kwargs.values())
        values.append(model_id)
        values = tuple(values)

        with cls.connection.cursor() as cursor:
            cursor.execute(sql_set, values)
        cls.connection.commit()

    def __repr__(self):
        return json.dumps(self.__dict__)


def recreate_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password=password.password,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    sql_check_if_exist = 'DROP DATABASE IF EXISTS `{}`'.format(SQLModel.db_name)
    sql_create_database = 'CREATE DATABASE `{}` DEFAULT CHARACTER SET utf8mb4'.format(
        SQLModel.db_name
    )

    with connection.cursor() as cursor:
        log(sql_check_if_exist)
        cursor.execute(sql_check_if_exist)

        log(sql_create_database)
        cursor.execute(sql_create_database)
        cursor.execute('USE `{}`'.format(SQLModel.db_name))
        cursor.execute(SQLModel.sql_create)

    connection.commit()
    connection.close()


def insert_random_data():
    from random import randint

    with open('product.txt', mode='r', encoding='utf-8') as f:
        product = json.load(f)
    with open('location.txt', mode='r', encoding='utf-8') as f:
        location = json.load(f)

    for p in product:
        for l in location:
            price = randint(1, 999)
            form = dict(
                name=p,
                madeIn=l,
                price=price
            )

            m = SQLModel.new(form=form)
            log('', m)
    log('Date importing finished')


if __name__ == '__main__':
    recreate_database()
    insert_random_data()
