score = input('請輸入分數: ')

if(score.isdigit()):
    score = int(score)
    if score >= 60:
        print(str(score) + "及格")
    else:
        print(str(score) + "不及格")
else:
    print("資料錯誤")

