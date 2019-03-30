# 匯入套件資源:
import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 建立 sqlalchemy 基礎描述物件(基類):
Base = declarative_base()


# 定義 User 物件對象:
class User(Base):
    # 資料表名:
    __tablename__ = 'user'
    # 資料表欄位:
    id = Column('id', Integer, primary_key=True)
    name = Column(String(20), unique=True)
    ts = Column(DateTime, default=datetime.datetime.utcnow)


# 初始化資料庫連結:
engine = create_engine('sqlite:///demo.db', echo=True)

# 建立資料表
Base.metadata.create_all(bind=engine)