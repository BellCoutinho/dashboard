from psycopg2 import sql, OperationalError
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db

def save(doctor):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''INSERT INTO doctor(name, crm)
        VALUES({}, {})'''
        ).format(
            sql.Literal(doctor.name),
            sql.Literal(doctor.crm))

        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while insert the table doctor")
    connection.close()
    return doctor

def find_by_id(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = []
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT * FROM doctor
            WHERE id = {}
            '''
        ).format(
            sql.Literal(id))

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table doctor")
    connection.close()
    return result

def find_by_patient_id(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = []
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT d.* FROM patient
            INNER JOIN medical_record
            ON medical_record.id_patient = {}
            INNER JOIN doctor AS d
            ON medical_record.id_doctor = d.id
            '''
        ).format(
            sql.Literal(id)
        )

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table doctor")
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
            '''
            SELECT * FROM doctor
            ''')

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchall()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table doctor")
    connection.close()
    return result

def update(doctor, id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            UPDATE doctor
            SET name = {},
                crm = {}
            WHERE id = {}
            ''').format(
                sql.Literal(doctor.name),
                sql.Literal(doctor.crm),
                sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while the updated table doctor")
    connection.close()
    return doctor

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
                CASE WHEN EXISTS(select 1 from doctor
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
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while search on table doctor")
    connection.close()
    return result

def delete(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            DELETE FROM doctor
            WHERE id = {}
            '''
        ).format(
            sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while deleted element of table doctor")
    connection.close()
