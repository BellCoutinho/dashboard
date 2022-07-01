from psycopg2 import sql, OperationalError
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db

def save(medical_record):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            INSERT INTO medical_record(date, time, medical_notes, id_doctor, id_patient)
            VALUES({}, {}, {}, {}, {})
            '''
        ).format(
            sql.Literal(medical_record.date),
            sql.Literal(medical_record.time),
            sql.Literal(medical_record.medical_notes),
            sql.Literal(medical_record.doctor),
            sql.Literal(medical_record.patient)
        )

        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while insert the table medical_record")
    connection.close()
    return medical_record

def find_by_id(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = []
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT * FROM medical_record
            WHERE id = {}
            '''
        ).format(
            sql.Literal(id))

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table medical_record")
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
            SELECT m.* FROM medical_record AS m
            LEFT JOIN patient as p
            ON m.id_patient = {}
            '''
        ).format(
            sql.Literal(id))

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchone()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table medical_record")
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
            SELECT * FROM medical_record
            ''')

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchall()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table medical_record")
    connection.close()
    return result

def update(medical_record, id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            UPDATE medical_record
            SET date = {},
                time = {},
                medical_notes = {},
                id_doctor = {},
                id_patient = {}
            WHERE id = {}
            ''').format(
                sql.Literal(medical_record.date),
                sql.Literal(medical_record.time),
                sql.Literal(medical_record.medical_notes),
                sql.Literal(medical_record.doctor),
                sql.Literal(medical_record.patient),
                sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while the updated table medical_record")
    connection.close()
    return  medical_record

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
                CASE WHEN EXISTS(select 1 from medical_record
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
            print("An error occurred while search the medical_record")
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
            DELETE FROM medical_record
            WHERE id = {}
            '''
        ).format(
            sql.Literal(id))
        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while deleted element of table medical_record")
    connection.close()
