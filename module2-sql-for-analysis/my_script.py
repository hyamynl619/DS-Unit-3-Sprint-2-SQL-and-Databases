
import pyscopg2

print("CONNECTING TO THE DATABASE...")

conn = psycopg2.connect(
    dbname = 'dtbvkzle',
    user= 'dtbvkzle',
    password='M6VvGo-LtzJjqh6oqErwJmwQ7VM53doZ',
    host= 'rajje.db.elephantsql.com'
)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

cursor.execute('SELECT * test_table;')
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)