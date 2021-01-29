import psycopg2
from psycopg2 import OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = 'postgres'
PASS = 'mati2000'
DB_HOST = 'localhost'
DB_NAME = 'postgres'

sql = f"""
    CREATE DATABASE workshop_db;
"""
users_table = f"""
    CREATE TABLE users(
    id serial,
    username varchar(255),
    hashed_password varchar(80),
    PRIMARY KEY (id)
    );
"""
messages_table = f"""
    CREATE TABLE messages(
    id serial,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

try:
    conn = psycopg2.connect(user=USER, password=PASS, host=DB_HOST, database=DB_NAME)
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        print('DB created')
    except DuplicateDatabase as e:
        print('This DB already exists', e)

    conn.close()

except OperationalError as e:
    print('Error with connection', e)

try:
    conn = psycopg2.connect(user=USER, password=PASS, host=DB_HOST, database='workshop_db')
    conn.autocommit = True
    cursor = conn.cursor()

    try:
        cursor.execute(users_table)
        print('Table created')
    except DuplicateTable as e:
        print('This Table already exists', e)

    try:
        cursor.execute(messages_table)
        print('Table created')
    except DuplicateTable as e:
        print('This Table already exists', e)


    conn.close()


except OperationalError as e:
    print('Error with connection', e)
