def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operation(func, x):
    return func(x)

print(operation(inc, 2))
print(operation(dec, 2))