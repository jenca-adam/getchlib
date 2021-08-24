import threading 
try:    
    from .getkey import getkey
except ImportError:
    from getkey import  getkey
try:
    from .decorators import with_args
except ImportError:
    from decorators import with_args
try:
    from . import term
except ImportError:
    try:
        import term
    except ImportError:
        term=None
try:
    from .ctrl import CTRLIN
except ImportError:
    from ctrl import CTRLIN
class HotKeyListener:
    def __init__(self,catch=False):
        self.hotkeys={}
        self.catch=catch
        self.__quit=False
        self.blocking=True
        self.__thread=threading.Thread(target=self.__blocking,args=(lambda:self.__quit,))
    def __blocking(self,destroy):
        while not destroy():
            try:
                key=getkey(False,tout=0.1,catch=self.catch)
            except:
                break
            term.buffering.on()
            if hasattr(key,'char'):
                key=key.char
            if key in self.hotkeys:
                self.hotkeys[key]()
            if key=='\x03':
                if not self.catch:
                    raise KeyboardInterrupt
        term.buffering.on()

    def add_hotkey(self,key,emit,*args,**kwargs):
        if not callable(emit):
            raise TypeError(
                'add_hotkey() argument 2 must be a function (got type '+str(type(emit))+')'
                )
        if key.upper() in CTRLIN:
            key=CTRLIN[key.upper()]
        self.hotkeys[key]=with_args(*args,**kwargs)(emit)
    def _start(self):
        self.__thread.start()
    def join(self,*a):
        self.__thread.join(*a)
    def terminate(self):
        self.__quit=True
    def start(self):
        try:
            self._start()
            if self.blocking:
                self.join()
        finally:
            self.terminate()
            if term:
                term.buffering.on()

