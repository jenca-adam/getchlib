from .key import KeyboardEvent
from .term import buffering, Buffering
from .parsers.unix import parse_key

import sys
import tty
import termios
import os
import time
import fcntl
import select
from collections import deque
from typing import IO

_event_buffer: deque = deque()


def _getkey(
    blocking: bool = True,
    tout: float | int = 0.0,
    catch: bool = False,
    echo: bool = False,
) -> str:
    key = ""
    with Buffering(sys.stdin):
        try:
            while True:
                ev, _, _ = select.select(
                    [sys.stdin], [], [], (tout if not blocking else None)
                )
                if ev:
                    key = _readmax(sys.stdin)
                    break
                else:
                    if not blocking:
                        break
        except KeyboardInterrupt:
            if not catch:
                raise
            key += "\x03"

    if key.isprintable() and echo:
        buffering.on()

        print(key, end="", flush=True)
    return key


def getkey(
    blocking: bool = True,
    tout: float | int = 0.0,
    catch: bool = False,
    echo: bool = False,
    buffer: bool = True,
) -> KeyboardEvent | None:
    if buffer and _event_buffer:
        return _event_buffer.popleft()
    else:
        _event_buffer.clear()  # to avoid de-syncing
    try:
        code = _getkey(blocking, tout, catch, echo)
        event, end = parse_key(code)
        code = code[end:]
        while code and buffer:
            buf_event, end = parse_key(code)
            _event_buffer.append(buf_event)
            code = code[end:]
        return event
    finally:
        buffering.on()


def _addflag(fp: IO, fl: int, add: bool = True) -> None:
    fn = fp.fileno()
    flag = fcntl.fcntl(fn, fcntl.F_GETFL)
    if add:
        nflag = flag | fl
    else:
        nflag = flag & ~fl
    fcntl.fcntl(fn, fcntl.F_SETFL, nflag)


def _readmax(fp: IO) -> str:
    out = b""
    while True:
        ev, _, _ = select.select([fp], [], [], 0)
        if not ev:
            break
        out += os.read(fp.fileno(), 8)
    return out.decode("utf-8")
