import msvcrt
from .ctrl import *


def getkey(blocking=True, tout=0.1, catch=False, echo=False):
    if not blocking:
        if msvcrt.kbhit():
            key = msvcrt.getch()
        else:
            key = b""
    else:
        try:
            key = msvcrt.getch()
        except KeyboardInterrupt:
            if not catch:
                raise
            key = b"\x03"
    key = str(key)[1:]  # ugly but whatever
    if key.isprintable() and echo:
        print(key, end="", flush=True)
    return parse_key(key)
