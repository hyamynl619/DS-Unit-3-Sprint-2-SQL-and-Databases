import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # > loads contents of the .env file into the script's environment

DB_NAME = 'dtbvkzle'
DB_USER = 'dtbvkzle'
DB_PASSWORD = 'M6VvGo-LtzJjqh6oqErwJmwQ7VM53doZ'
DB_HOST = 'rajje.db.elephantsql.com'

connection = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)
cursor.execute('SELECT * from test_table;')

result = cursor.fetchall()
print("RESULT:", type(result))
print(result)
