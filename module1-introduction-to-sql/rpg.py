
import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
cur = conn.cursor()

# How Many total characters are there?

query = 'SELECT * FROM charactercreator_character;'
character_total = len(cur.execute(query).fetchall())
print(character_total)

# How many of each specific subclass?

query = 'SELECT * FROM charactercreator_mage;'
mage = len(cur.execute(query).fetchall())
print(mage)

query = 'SELECT * FROM charactercreator_thief;'
thief = len(cur.execute(query).fetchall())
print(thief)

query = 'SELECT * FROM charactercreator_cleric;'
cleric = len(cur.execute(query).fetchall())
print(cleric)

query = 'SELECT * FROM charactercreator_fighter;'
fighter = len(cur.execute(query).fetchall())
print(fighter)

# How many total items?

query = 'SELECT * FROM armory_item'
total_items = len(cur.execute(query).fetchall())
print('Total Items: ', total_items)

# How many of the Items are weapons? How many are not?

query = 'SELECT * FROM armory_weapon;'
weapon = len(cur.execute(query).fetchall())
print('Weapons: ', weapon)

query = 'SELECT * FROM armory_item;'
not_weapon = (len(cur.execute(query).fetchall()) - weapon)
print('Not A Weapon: ', not_weapon)

# How many Items does each character have? (Return first 20 rows)

query = '''
        SELECT cc.character_id cid, COUNT(charactercreator_character_inventory.item_id) AS NumOfItems
        FROM charactercreator_character as cc LEFT JOIN charactercreator_character_inventory ON cid =
        charactercreator_character_inventory.character_id GROUP BY cid LIMIT 20
        '''
items_per_char = len(cur.execute(query).fetchall())
print('Total Items Per Character: ', items_per_char)

# How many weapons does each character have? (Return first 20 Rows)

query = '''
        SELECT cc.character_id, COUNT(ci.item_id)
        FROM charactercreator_character as cc,
        charactercreator_character_inventory as ci,
        armory_item as ai
        WHERE cc.character_id = ci.character_id
        AND ci.item_id = ai.item_id
        AND ai.item_id IN (SELECT item_ptr_id FROM armory_weapon)
        GROUP BY cc.character_id LIMIT 20
        '''

weapons_per_char = len(cur.execute(query).fetchall())
print('Total Weapons Per Character: ', weapons_per_char)

# On average, how many Items does each Character have?

query = '''
        SELECT AVG( NumOfItems )
        FROM (SELECT cc.character_id cid,
        COUNT(charactercreator_character_inventory.item_id) AS
        NumOfItems FROM charactercreator_character as cc 
        LEFT JOIN charactercreator_character_inventory ON cid = charactercreator_character_inventory.character_id 
        GROUP BY cid
        '''

avg_items_per_char = len(cur.execute(query).fetchall())
print('Average items per character, ', avg_items_per_char)


# On average, how many Weapons does each character have?
query = '''
        SELECT AVG( NumOfItems )FROM (SELECT cc.character_id cid,
        COUNT(charactercreator_character_inventory.item_id) AS NumOfItems FROM charactercreator_character as cc LEFT JOIN charactercreator_character_inventory ON cid = charactercreator_character_inventory.character_id GROUP BY cid'''

avg_items_per_char = len(cur.execute(query).fetchall())
print('Average items per character, ', avg_items_per_char)
