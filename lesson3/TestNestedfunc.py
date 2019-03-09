def print_msg(msg):  # outer enclosing function
    def printer():   # nested function
        print(msg)
    printer()

print_msg("Hello")

def add(x):
    def func(y):
        return x + y
    return func

print(add(2)(3))