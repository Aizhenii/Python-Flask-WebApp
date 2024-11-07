import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
  "INSERT INTO clubs (club, category, location, provide, looking, description, contact) VALUES (?, ?, ?, ?, ?, ?, ?)",
  (
    'First Club',
    'Content for the first post',
  ))

cur.execute(
  "INSERT INTO businesses (business, location, provide, looking, description, contact) VALUES (?, ?, ?, ?, ?, ?)",
  ('Second Club', 'Content for the second post'))

connection.commit()
connection.close()
