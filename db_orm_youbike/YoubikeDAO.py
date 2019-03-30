# 匯入套件資源:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_orm_youbike.Create import Youbike
import db_orm_youbike.YoubikeUtil as util


def import_data():
    list = util.get_youbike_list()
    # 初始化資料庫連結:
    engine = create_engine('sqlite:///demo.db', echo=True)
    # 創建 DBSession:
    DBSession = sessionmaker(bind=engine)
    # 創建 session 物件對象:
    session = DBSession()

    # 新增 ------------------------------------------------------
    for youbike in list:
        new_youbike = Youbike(
            sno = youbike.get('sno'),
            sna = youbike.get('sna'),
            tot = youbike.get('tot'),
            sbi = youbike.get('sbi'),
            bemp = youbike.get('bemp'),
            lat = youbike.get('lat'),
            lng = youbike.get('lng')
        )
        session.add(new_youbike)

    # 提交到資料庫中儲存:
    session.commit()
    # 關閉 session:
    session.close()


def delete_all():
    engine = create_engine('sqlite:///demo.db', echo=False)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        session.query(Youbike).delete()
        session.commit()
    except Exception as e:
        print(e)

    session.close()


