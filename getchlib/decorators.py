import functools
def with_args(*a,**k):
    def decorator(fun):
        @functools.wraps(fun)
        def inner(*a2,**k2):
            return fun(*a,*a2,**k,**k2)
        return inner
    return decorator
