import ctypes
from collections import deque
from .parsers.windows import parse_key
from .key import KeyboardEvent
from typing import Optional

msvcrt = ctypes.CDLL("msvcrt")
_event_buffer: deque = deque()


def getkey(
    blocking: bool = True,
    tout: float | int = 0.0,
    catch: bool = False,
    echo: bool = False,
    buffer: bool = True,
) -> Optional[KeyboardEvent]:
    if buffer and _event_buffer:
        return _event_buffer.popleft()
    else:
        _event_buffer.clear()
    if echo:
        getch = msvcrt._getche
    else:
        getch = msvcrt._getch
    if not blocking:
        key = []
        while msvcrt._kbhit():
            key.append(abs(getch()))
    else:
        try:
            key = [abs(getch())]
            while msvcrt._kbhit():
                key.append(abs(getch()))

        except KeyboardInterrupt:
            if not catch:
                raise
            key = [3]
    event, end = parse_key(key)
    key = key[end:]
    while key and buffer:
        buf_event, end = parse_key(key)
        _event_buffer.append(buf_event)
        key = key[end:]
    return event
