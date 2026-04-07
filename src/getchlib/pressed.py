from .getkey import getkey


def pressed(self):
    while True:
        key = getkey(blocking=False)
        if not key:
            break
        yield key
