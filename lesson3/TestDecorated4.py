import logging


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warning":
                logging.warning("%s is running" % func.__name__)
            elif level == "error":
                logging.error("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator


@use_logging(level="warning")
def foo(name, weight=None, height=None):
    print("I am %s, weight %s, height %s" % (name, weight, height))

@use_logging(level="error")
def foo2(name, weight=None, height=None):
    print("I am %s, weight %s, height %s" % (name, weight, height))


print(foo('Vincent', 60, 170))
print(foo2('Vincent', 60, 170))
