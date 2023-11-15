try:
    from . import term
except:
    term=None
from .getkey import getkey
from .decorators import with_args
from .ctrl import CTRLIN
import os
def _bo():
    if term is not None:
        term.buffering.on()
class HotKeyListener:
    def __init__(self,catch=False,blocking=True):
        self.hotkeys={}
        self.catch=catch
        self.__quit=False
        self.blocking=blocking
        if not blocking:
            if os.name!='posix':
                raise SystemError('Non-blocking mode available only on Linux systems.')
    def __blocking(self,destroy):
        while not destroy():
            try:
                key=getkey(False,tout=0.1,catch=self.catch)
            except:
                break
            _bo()
            if hasattr(key,'char'):
                key=key.char
            if key in self.hotkeys:
                self.hotkeys[key]()
            if key=='\x03':
                if not self.catch:
                    raise KeyboardInterrupt
        _bo()

    def add_hotkey(self,key,emit,*args,**kwargs):
        if not callable(emit):
            raise TypeError(
                'add_hotkey() argument 2 must be a function (got type '+str(type(emit))+')'
                )
        if key.upper() in CTRLIN:
            key=CTRLIN[key.upper()]
        self.hotkeys[key]=with_args(*args,**kwargs)(emit)
    def _start(self):
        self.__blocking(lambda:False) 
    def join(self,*a):
        self.__thread.join(*a)
    def terminate(self):
        self.__quit=True
    def start(self):
        if not self.blocking:
            if os.fork():
                self._start()
        else:
            try:
                self._start()
            finally:
                _bo() 
