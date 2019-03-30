import os
import db_orm_youbike.YoubikeDAO as dao
import db_orm_youbike.YoubikeUtil as util

def menu():
    clear_screen()
    print("台北市 Youbike 出借查詢系統")
    print("------------------------")
    print("1. 資料同步")
    print("2. 列出所有站點資料")
    print("3. 取出某站號或站名的資料")
    print("4. 我要借 N 台")
    print("5. 我要還 N 台")
    print("6. 我要借 N 還 N 台")
    print("------------------------")
    print("0. 結束電腦選號程式")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':

    while True:
        menu()
        choice = int(input('請輸入您的選擇 : '))
        if choice == 1:
            dao.delete_all()
            dao.import_data()
        elif choice == 2:
            youbikes = dao.query_all()
            util.print_youbike(youbikes)
        elif choice == 3:
            youbikes = dao.query_by(input('請輸入站號或站名 : '))
            util.print_youbike(youbikes)
        elif choice == 4:
            youbikes = dao.query_sbi(int(input('我要借(台) : ')))
            util.print_youbike(youbikes)
        elif choice == 5:
            youbikes = dao.query_bemp(int(input('我要還(台) : ')))
            util.print_youbike(youbikes)
        elif choice == 6:
            sbi, bemp = input('我要借(台), 還(台): 例如:30 30 => ').split()
            youbikes = dao.query_sbi_bemp(int(sbi), int(bemp))
            util.print_youbike(youbikes)
        elif choice == 0:
            break
        input('按任意鍵返回主選單')

