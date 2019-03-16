import db.modu.SQLModu as m

conn, cursor = m.connect('../demo.db')

m.insert_lotto(cursor, conn)
m.select_lotto(cursor)

m.close(conn)

