from psycopg2 import sql, OperationalError
from src.infra.db.postgres import postgres_connection
from src.infra.db.config import Db

def save(image, id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            INSERT INTO image(filename, date, image64, id_patient)
            VALUES({}, {}, {}, {})
            '''
        ).format(
            sql.Literal(image.filename),
            sql.Literal(image.date),
            sql.Literal(image.image64),
            sql.Literal(id)
        )

        try:
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while insert the table medical_record")
    connection.close()
    return image

def find_last(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                     Db.USER_NAME,
                                     Db.PASSWORD,
                                     Db.HOST)
    result = []
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT i.* FROM image AS i
            LEFT JOIN patient as p
            ON i.id_patient = {}
            ORDER BY i.date DESC
            LIMIT 1;
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

def find_all(id):
    connection = postgres_connection(Db.DATABASE_NAME,
                                    Db.USER_NAME,
                                    Db.PASSWORD,
                                    Db.HOST)
    result = []
    with connection.cursor() as cursor:
        sql_statements = sql.SQL(
            '''
            SELECT i.* FROM image AS i
            LEFT JOIN patient as p
            ON i.id_patient = {}
            ORDER BY i.date DESC
            ''').format(
                sql.Literal(id))

        try:
            cursor.execute(sql_statements)
            result = cursor.fetchall()
        except OperationalError as e:
            print(e)
            print("An error occurred while the search table doctor")
    connection.close()
    return result


