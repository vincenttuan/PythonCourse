# 匯入套件資源:
import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 建立 sqlalchemy 基礎描述物件(基類):
Base = declarative_base()


# 定義 User 物件對象:
class Youbike(Base):
    # 資料表名:
    __tablename__ = 'youbike'
    # 資料表欄位:
    sno  = Column('sno', String(10), primary_key=True)
    sna  = Column(String(50), unique=True)
    tot  = Column(Integer)
    sbi  = Column(Integer)
    bemp = Column(Integer)
    lat  = Column(Float)
    lng  = Column(Float)
    ts   = Column(DateTime, default=datetime.datetime.now)


# 初始化資料庫連結:
engine = create_engine('sqlite:///demo.db', echo=True)

# 建立資料表
Base.metadata.create_all(bind=engine)
