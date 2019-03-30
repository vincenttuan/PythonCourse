class LoginException(Exception):
    def __init__(self, message) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


def login(username, password):
    if username == 'admin' and password == '1234':
        print('Pass')
    else:
        raise LoginException('登入錯誤')

try:
    login('admin', '1234')
except LoginException as e:
    print(e)

try:
    login('admin', '5678')
except LoginException as e:
    print(e)

try:
    login('admin', '8888')
except LoginException as e:
    print('我不玩了')


