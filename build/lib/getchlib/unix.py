import sys
import tty
import termios
import os
import time
import fcntl
import select
from .term import buffering, Buffering
from .ctrl import *
import sys


class NoBufReader:
    def __init__(self, file):
        self.fileno = file.fileno
        self.encoding = file.encoding
        self.fd = self.fileno()
        self.file = file

    def read(self, size):
        return self.file.read(size)


def _getkey(blocking=True, tout=0.1, catch=False, echo=False):
    key = ""
    with Buffering(sys.stdin):
        try:
            while True:
                ev, _, _ = select.select(
                    [sys.stdin], [], [], (tout if not blocking else 0)
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


def getkey(blocking=True, tout=0.1, catch=False, echo=False):
    try:
        return parse_key(_getkey(blocking, tout, catch, echo))
    finally:
        buffering.on()


def _addflag(fp, fl, add=True):
    fn = fp.fileno()
    flag = fcntl.fcntl(fn, fcntl.F_GETFL)
    if add:
        nflag = flag | fl
    else:
        nflag = flag & ~fl
    fcntl.fcntl(fn, fcntl.F_SETFL, nflag)


def _readmax(fp):
    out = b""
    while True:
        ev, _, _ = select.select([fp], [], [], 0)
        if not ev:
            break
        out += os.read(fp.fileno(), 8)
    return out.decode("utf-8")
