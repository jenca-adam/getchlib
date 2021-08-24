import termios
import tty
import sys
class Buffering:

    def __init__(self,file):
        self.fd=file.fileno()
        self.file=file
        self.settings=termios.tcgetattr(file)
    def on(self):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.settings)
    def off(self):
        tty.setcbreak(self.file)
    def __enter__(self,*foo):
        self.off()
    def __exit__(self,*foo):
        self.on()
buffering=Buffering(sys.stdin)
