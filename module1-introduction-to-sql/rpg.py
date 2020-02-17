
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

#How Many total characters are there?

query = 'SELECT * FROM charactercreater_character;'
character_total = len(cur.execute(query).fetchall())
print(characters)