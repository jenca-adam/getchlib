import sys
import tty
import termios
import os
import time
import fcntl
from .term import buffering,Buffering
from .ctrl import *
import sys
class NoBufReader:
    def __init__(self,file):
        self.fileno=file.fileno
        self.encoding=file.encoding
        self.fd=self.fileno()
        self.file=file
    def read(self,size):
        return self.file.read(size)

def _getkey_nonblocking(tout=0.1,catch=False,echo=False):
    char=''
    buffer=buf(NoBufReader(sys.stdin),catch)
    e=False
    _time=time.time()
    _end=_time+tout
    while time.time()<=_end:
        try:
            a=next(buffer)
            if a:
                if not e:
                    e=True
                char+=a
            else:
                if e:
                    break
        except KeyboardInterrupt:
            if not catch:
                raise
            if not e:
                e=True
            char+='\x03'
            
    return char

def _getkey_blocking(tout=0.01,catch=False,echo=False):
    char=''
    buffer=buf(NoBufReader(sys.stdin),catch)
    entering=False
    for c in buffer:
        if not c:
            if entering:
                break
        else:
            if not entering:
                entering=True
            char+=c
    return char
            

def _getkey(blocking=True,tout=0.1,catch=False,echo=False):
    if blocking:
        
        key= _getkey_blocking(tout,catch)
    else:
        
        key = _getkey_nonblocking(tout,catch)
   
    if key.isprintable() and echo:
        term.buffering.on()

        print(key,end='',flush=True)
    return key
def getkey(blocking=True,tout=0.1,catch=False,echo=False):
    try:
        return parse_key(_getkey(blocking,tout,catch,echo))
    except KeyboardInterrupt:
            if not catch:
                raise
            if not entering:
                entering=True
            char+='\x03'

    finally:
        flag = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
        fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, flag & ~os.O_NONBLOCK) # remove the non-blocking flag (fix #1)
        buffering.on()
def buf(file,catch=False):
    fcntl.fcntl(file, fcntl.F_SETFL, os.O_NONBLOCK)

    with Buffering(file):
        while True:
            try:
                a=file.read(1)
            except KeyboardInterrupt:
                if not catch:
                    raise
                a='\x03'
            yield a
