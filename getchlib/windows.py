import msvcrt
from .ctrl import *
def getkey(blocking=True,tout=0.1,catch=False):
    if not blocking:
        if msvcrt.kbhit():
            key=msvcrt.getch()
    else:
        try:
            key=msvcrt.getch()
        except KeyboardInterrupt:
            if not catch:
                raise
            key='\x03'
    return parse_key(key)
