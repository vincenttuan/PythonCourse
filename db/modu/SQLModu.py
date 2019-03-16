import sqlite3
import random
import datetime

def connect(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()
    return conn, cursor


def close(conn):
    conn.close()


def select_lotto(cursor):
    print_header(cursor)
    # 查詢資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto'
    # select case 1
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


def select_lotto_one(cursor):
    print_header(cursor)
    # 查詢資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto ORDER BY Random() LIMIT 1'
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is not None:  # if not row == None
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


def select_lotto_many(cursor, n):
    print_header(cursor)
    # 查詢資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto ORDER BY Random() LIMIT {}'.format(n)
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


def print_header(cursor):
    print('-----------------------------------------------')
    # 查詢 Table META-INFO
    cursor.execute('PRAGMA TABLE_INFO({})'.format('lotto'))
    names = [tup[1] for tup in cursor.fetchall()]
    for name in names:
        print(name, end='\t')
    print('\n-----------------------------------------------')


def insert_lotto(cursor, conn):
    sql = 'INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES(?, ?, ?, ?, ?, ?)'
    # 取出 1~46 不重複的數字六個
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 46))
    # sql, (args...)
    cursor.execute(sql, (nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop()))  # 執行 SQL 語句
    conn.commit()


def insert_lotto_self(cursor, conn, *args):
    if len(args) == 6:
        sql = 'INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES(?, ?, ?, ?, ?, ?)'
        cursor.execute(sql, (args[0], args[1], args[2], args[3], args[4], args[5]))
        conn.commit()


def update_lotto(cursor, conn, id):
    # 1.查詢欲修改 id 資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto WHERE id = {}'.format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is not None:  # if not row == None
        print(
            '修改前：{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    # 2.修改程序
    sql = 'Update lotto SET n1=?, n2=?, n3=?, n4=?, n5=?, n6=?, ts=? WHERE id=?'
    now = datetime.datetime.now()
    # 重新產生 1~46 不重複的數字六個
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 46))
    # sql, (args...)
    cursor.execute(sql, (nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop(), nums.pop(), now, id))  # 執行 SQL 語句
    conn.commit()

    # 3.查詢欲修改後 id 資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto WHERE id = {}'.format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is not None:  # if not row == None
        print('修改後：{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    print('修改 id=%d 資料成功 !' % id)


def delete_lotto(cursor, conn, id):

    # 刪除程序
    sql = 'DELETE FROM lotto WHERE id={}'.format(id)
    cursor.execute(sql)  # 執行 SQL 語句
    conn.commit()

    print('刪除 id=%d 資料成功 !' % id)


def analysis(cursor):
    # 查詢資料列 SQL
    sql = 'SELECT id, n1, n2, n3, n4, n5, n6, ts FROM lotto'
    cursor.execute(sql)
    rows = cursor.fetchall()

    lst = [0] * 47
    for row in rows:
        lst[row[1]] += 1
        lst[row[2]] += 1
        lst[row[3]] += 1
        lst[row[4]] += 1
        lst[row[5]] += 1
        lst[row[6]] += 1

    print(lst)

    for idx, val in enumerate(lst):
        if idx == 0:
            continue
        print('%02d : ' % idx, end='')
        for x in range(val):
            print("*", end='')
        print(' (%d %.5f %.5f)' % (val, val/sum(lst), 1/46))

    print()
    print("max = %d(%d)" % (lst.index(max(lst)), max(lst)))
    print()
