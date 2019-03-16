import sqlite3

sql = 'create table if not exists lotto (' \
      'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
      'n1 INTEGER, ' \
      'n2 INTEGER, ' \
      'n3 INTEGER, ' \
      'n4 INTEGER, ' \
      'n5 INTEGER, ' \
      'n6 INTEGER, ' \
      'ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()  # 建立 cursor
cursor.execute(sql)  # 建立 lotto 資料表

conn.commit()  # 執行資料庫更新
conn.close()
print('建立成功')
