import sqlite3

conn = sqlite3.connect('demo.db')
print(conn)
conn.close()
