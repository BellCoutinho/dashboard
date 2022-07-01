from psycopg2 import connect, extensions, sql, OperationalError
import sys
from .config import Db

def postgres_connection(database_name, user_name, password, host='localhost'):
    try:
        connetion = connect(
            dbname = f'{database_name}',
            user = f'{user_name}',
            host = host,
            password = f'{password}')
    except OperationalError as e:
            print(f'Unable to connect!\n{e}')
            sys.exit(1)
    return connetion

def create_application_database(database_name, user_name, password):
    connection = postgres_connection('postgres', 'postgres', 'postgresql')
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    connection.set_isolation_level(autocommit)

    with connection.cursor() as cursor:
        drop_database = f"""DROP DATABASE IF EXISTS {database_name};"""
        drop_user = f"""DROP USER IF EXISTS {user_name};"""
        create_database_if_not_exist = f"""CREATE DATABASE {database_name};"""
        crete_user = f"""
        CREATE USER {user_name} WITH PASSWORD 'password';
        GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {user_name};
        """
        try:
            cursor.execute(drop_database)
            cursor.execute(drop_user)
            cursor.execute(create_database_if_not_exist)
            cursor.execute(crete_user)
            connection.commit()
        except OperationalError as e:
            print(f'Unable to connect!\n{e}')
            print("An error occurred while creating the database")
            sys.exit(1)
    connection.close()

def create_entities():
    create_application_database(Db.DATABASE_NAME, Db.USER_NAME, Db.PASSWORD)
    connection = postgres_connection(Db.DATABASE_NAME, Db.USER_NAME, Db.PASSWORD)
    sql_statements = ''
    with connection.cursor() as cursor:
        try:
            sql_statements += create_patient()
            sql_statements += create_doctor()
            sql_statements += create_medical_record()
            sql_statements += create_image()
            cursor.execute(sql_statements)
            sql_statements = alter_medical_record()
            sql_statements += alter_image()
            cursor.execute(sql_statements)
            connection.commit()
        except OperationalError as e:
            print(e)
            print("An error occurred while creating the table")
    connection.close()

def create_patient():
    sql = """CREATE TABLE IF NOT EXISTS patient(
        id serial primary key,
        name varchar(100) not null,
        phone_number varchar(20),
        cpf varchar(11) not null unique);
    """

    return sql

def create_doctor():
    sql = """CREATE TABLE IF NOT EXISTS doctor(
    id serial primary key,
    name varchar(100) not null,
    crm varchar(11) unique not null);"""

    return sql

def create_medical_appointment():
    sql = """CREATE TABLE IF NOT EXISTS medical_appointment(
    id serial primary key,
    date date not null,
    time time not null,
    medical_notes text not null);"""

    return sql

def create_medical_record():
    sql = """CREATE TABLE IF NOT EXISTS medical_record(
    id serial primary key,
    date date not null,
    time time not null,
    medical_notes text not null,
    id_doctor integer not null,
    id_patient integer not null);"""

    return sql
def create_image():
    sql = """CREATE TABLE IF NOT EXISTS image(
    id serial primary key,
    filename varchar(200) not null,
    date date not null,
    image64 text not null,
    id_patient integer not null);"""

    return sql

def alter_medical_record():
    sql = """ALTER TABLE medical_record
    ADD FOREIGN KEY (id_doctor) REFERENCES doctor(id),
    ADD FOREIGN KEY (id_patient) REFERENCES patient(id);"""

    return sql

def alter_image():
    sql = """ALTER TABLE image
    ADD FOREIGN KEY (id_patient) REFERENCES patient(id);"""

    return sql

#create_entities('dashboard', 'user_dashboard', 'password')
create_entities()

