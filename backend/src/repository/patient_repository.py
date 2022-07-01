from psycopg2 import sql, OperationalError
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db

def save(patient):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''INSERT INTO patient(name, phone_number, cpf)
        VALUES({}, {}, {})'''
        ).format(
            sql.Literal(patient.name),
            sql.Literal(patient.phone_number),
            sql.Literal(patient.cpf))

        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()
    return patient

def find_by_id(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = ()
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''SELECT * FROM patient
            WHERE id = {}'''
        ).format(
            sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()
    return result

def find_all():
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = ()
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''SELECT * FROM patient''')
        try:
            cursor.execute(sql_statements)
            result = cursor.fetchall()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()
    return result

def exists_by_id(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = ()
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT
                CASE WHEN EXISTS(select 1 from patient
                                 where id = {})
                                 then
                                    TRUE
                                 ELSE
                                    FALSE
                                 END;
            '''
        ).format(
            sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            result = cursor.fetchall()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()
    return result

def update(patient, id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            UPDATE patient
            SET name = {},
                phone_number = {},
                cpf = {}
            WHERE id = {}
            '''
        ).format(
            sql.Literal(patient.name),
            sql.Literal(patient.phone_number),
            sql.Literal(patient.cpf),
            sql.Literal(id))

        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while updated the table patient")
    connection.close()
    return patient



def delete(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            DELETE FROM patient
            WHERE id = {}
            '''
        ).format(
            sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()
