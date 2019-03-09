import logging

# log
def use_logging(func):
    def wrapper(*a):
        logging.warning("%s is running" % func.__name__)
        return func(*a)
    return wrapper

# 檢驗程式碼
def verify(func):
    def inner(a, b):
        if b == 0:
            print("分母不得為0")
            return
        return func(a,b)
    return inner

# 執行商業邏輯
@use_logging
@verify
def divide(a,b):
    return a/b

print(divide(2,5))
