import functools


def now():
    print("now")


def log(text):
    def decrator(func):
        @functools.wraps
        def wrapper(*args, **kw):
            print("call (%s)" % func.__name__)
            return func(*args, **kw)

        return wrapper

    return decrator

now()
