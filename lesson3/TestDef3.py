def change(s):
    s[0] = int(s[0] * 1.1);
    s[1] = int(s[1] * 1.1);
    s[2] = int(s[2] * 1.1);

score = [90, 80, 70]
change(score)
print(score)
#--------------------------------
x = 0 # 全域變數
def updateX():
    #x = 100  # 區域變數
    global x # 全域宣告
    x = 100  # 修改全域變數內容

updateX()
print(x)