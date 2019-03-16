import sqlite3
import random

conn = sqlite3.connect('../demo.db')
cursor = conn.cursor()  # 建立 cursor

lottos = []

for i in range(100000):
    # 取出 1~46 不重複的數字六個
    nums = set()
    while len(nums) < 6:
        nums.add(random.randint(1, 46))

    lottos.append(tuple(nums)) # 要轉元組

print(lottos)

cursor.executemany('INSERT INTO lotto(n1, n2, n3, n4, n5, n6) VALUES (?,?,?,?,?,?)', lottos)

conn.commit()  # 執行資料庫更新
conn.close()
print('新增成功')
