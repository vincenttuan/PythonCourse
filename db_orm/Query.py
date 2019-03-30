# 匯入套件資源:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_orm.Create import User

# 初始化資料庫連結:
engine = create_engine('sqlite:///demo.db', echo=False)

# 創建 DBSession:
DBSession = sessionmaker(bind=engine)

# 創建 session 物件對象:
session = DBSession()

# 查詢 -----------------------------------------------------

# users = session.query(User).all()
# users = session.query(User).filter(User.id > 3)
users = session.query(User).filter(User.id > 3).filter(User.id < 5)
for user in users:
    print('%d %s %s' % (user.id, user.name, user.ts))

# ----------------------------------------------------------

# 關閉 session:
session.close()
