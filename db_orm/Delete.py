# 匯入套件資源:
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_orm.Create import User

# 初始化資料庫連結:
engine = create_engine('sqlite:///demo.db', echo=False)

# 創建 DBSession:
DBSession = sessionmaker(bind=engine)

# 創建 session 物件對象:
session = DBSession()

# 刪除 -----------------------------------------------------

try :
    users = session.query(User).all()
    for user in users:
        print('%d %s %s' % (user.id, user.name, user.ts))

    user = session.query(User).filter(User.id == 3).one()
    session.delete(user)

    # 提交到資料庫中儲存:
    session.commit()

    print("-----------------------------------------------")
    users = session.query(User).all()
    for user in users:
        print('%d %s %s' % (user.id, user.name, user.ts))
except :
    print('資料不存在')

# ----------------------------------------------------------

# 關閉 session:
session.close()
