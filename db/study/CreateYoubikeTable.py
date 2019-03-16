import sqlite3

# _id': 1,
# 'sarea': '中壢區',
# 'sareaen': 'Zhongli Dist.',
# 'sna': '中央大學圖書館',
# 'aren': 'No.300, Zhongda Rd.',
# 'sno': '2001',
# 'tot': '60',
# 'snaen': 'National Central University Library',
# 'bemp': '38',
# 'ar': '中大路300號(中央大學校內圖書館前)',
# 'act': '1',
# 'lat': '24.968128',
# 'lng': '121.194666',
# 'sbi': '21',
# 'mday': '20190316143820'

sql = 'create table if not exists youbike (' \
      '_id INTEGER PRIMARY KEY, ' \
      'sarea varchar(50), ' \
      'sareaen varchar(50), ' \
      'sna varchar(50), ' \
      'aren varchar(50), ' \
      'sno INTEGER, ' \
      'tot INTEGER, ' \
      'snaen varchar(50), ' \
      'bemp varchar(50), ' \
      'ar varchar(50), ' \
      'act INTEGER, ' \
      'lat FLOAT, ' \
      'lng FLOAT, ' \
      'sbi INTEGER, ' \
      'mday varchar(50), ' \
      'ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'

conn = sqlite3.connect('../demo.db')
cursor = conn.cursor()  # 建立 cursor
cursor.execute(sql)  # 建立 lotto 資料表

conn.commit()  # 執行資料庫更新
conn.close()
print('建立成功')
