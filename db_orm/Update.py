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

# 修改 -----------------------------------------------------

try :
    user = session.query(User).filter(User.id==3).one()
    print('修改前: %d %s %s' % (user.id, user.name, user.ts))
    user.name = 'Joe'
    user.ts = datetime.datetime.now()

    # 提交到資料庫中儲存:
    session.commit()

    user = session.query(User).filter(User.id == 3).one()
    print('修改後: %d %s %s' % (user.id, user.name, user.ts))
except :
    print('資料不存在')

# ----------------------------------------------------------

# 關閉 session:
session.close()
