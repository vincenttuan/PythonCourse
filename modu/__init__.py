import modu.Calc as c

__all__ = ['perf']

def perf(x, y):
    return c.add(x, y) * expr2(x, y)

def expr2(x, y):
    return c.div(x, y)


