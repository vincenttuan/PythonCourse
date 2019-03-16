import db.modu.SQLModu as m
import os

def menu():
    clear_screen()
    print("樂透（Lotto）電腦選號")
    print("-----------------")
    print("1. 產生新的一組號碼")
    print("2. 列出所有樂透號碼")
    print("3. 隨機取出一筆號碼")
    print("4. 隨機取出N筆號碼")
    print("5. 修改第N筆號碼")
    print("6. 刪除第N筆號碼")
    print("7. 分析號碼出現次數")
    print("0. 結束電腦選號程式")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

conn, cursor = m.connect('../demo.db')

if __name__ == '__main__':

    while True:
        menu()
        choice = int(input('請輸入您的選擇 : '))
        if choice == 1:
            m.insert_lotto(cursor, conn)
        elif choice == 2:
            m.select_lotto(cursor)
        elif choice == 3:
            m.select_lotto_one(cursor)
        elif choice == 4:
            n = int(input('請輸入顯示筆數 : '))
            m.select_lotto_many(cursor, n)
        elif choice == 5:
            id = int(input('請輸入欲修改id號碼 : '))
            m.update_lotto(cursor, conn, id)
        elif choice == 6:
            id = int(input('請輸入欲刪除id號碼 : '))
            m.delete_lotto(cursor, conn, id)
        elif choice == 7:
            m.analysis(cursor)
        elif choice == 0:
            break
        input('按任意鍵返回主選單')

    m.close(conn)
