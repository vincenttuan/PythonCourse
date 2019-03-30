# 匯入套件資源:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_orm.Create import User

# 初始化資料庫連結:
engine = create_engine('sqlite:///demo.db', echo=True)

# 創建 DBSession:
DBSession = sessionmaker(bind=engine)

# 創建 session 物件對象:
session = DBSession()

# 新增 ------------------------------------------------------
# 創建新的 User 物件對象:
# new_user = User(id=3, name='Vincent') # 自訂 id 值
# new_user = User(name='Vincent')  # id 會自動加 1
new_user = User(name=input('請輸入 User name : '))  # id 會自動加 1

# 加入一筆資料
session.add(new_user)

# ----------------------------------------------------------

# 提交到資料庫中儲存:
session.commit()

# 關閉 session:
session.close()
