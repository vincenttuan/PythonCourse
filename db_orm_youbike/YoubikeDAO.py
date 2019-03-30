# 匯入套件資源:
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import sessionmaker
from db_orm_youbike.Create import Youbike
import db_orm_youbike.YoubikeUtil as util


def import_data():
    # 取得所有資料
    list = util.get_youbike_list()
    # 取得 session 物件對象:
    session = util.get_db_session()
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
    # 取得 session 物件對象:
    session = util.get_db_session()
    try:
        session.query(Youbike).delete()
        session.commit()
    except Exception as e:
        print(e)

    session.close()


def query_all():
    # 取得 session 物件對象:
    session = util.get_db_session()
    # 查詢 -----------------------------------------------------
    youbikes = session.query(Youbike).all()
    # ----------------------------------------------------------
    # 關閉 session:
    session.close()
    return youbikes


def query_by(sno_sna):
    # 取得 session 物件對象:
    session = util.get_db_session()
    # 查詢 -----------------------------------------------------
    youbikes = session.query(Youbike).filter(or_(Youbike.sno.like('%' + sno_sna + '%'), Youbike.sna.like('%' + sno_sna + '%'))).all()
    # ----------------------------------------------------------
    # 關閉 session:
    session.close()
    return youbikes
