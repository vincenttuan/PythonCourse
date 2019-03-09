def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

#ordinary()

pretty = make_pretty(ordinary)
pretty()