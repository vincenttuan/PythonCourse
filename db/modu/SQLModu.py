import sqlite3
import random

def connect(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    return conn, cursor

def close(conn):
    conn.close()


def select_lotto(cursor):
    # 查詢 Table META-INFO
    cursor.execute('PRAGMA TABLE_INFO({})'.format('lotto'))
    names = [t[1] for t in cursor.fetchall()]
    for name in names:
        print(name, end='\t')

    print('\n-----------------------------------------------')

    # 查詢資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto'
    # select case 1
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

def insert_lotto(cursor, conn):
    sql = 'INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES(?, ?, ?, ?, ?, ?)'
    # 取出 1~46 不重複的數字六個
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 46))
    # sql, (args...)
    cursor.execute(sql, (nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop()))  # 執行 SQL 語句
    conn.commit()
