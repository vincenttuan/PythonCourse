def outer():
    x = 10
    def inner():
        print(x)
    x = 20
    return inner

f = outer()
f()
