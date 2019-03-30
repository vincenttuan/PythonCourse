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

try :
    user = session.query(User).filter(User.id==2).one()
    print('%d %s %s' % (user.id, user.name, user.ts))
except :
    print('資料不存在')

# ----------------------------------------------------------

# 關閉 session:
session.close()
