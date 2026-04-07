import termios
import tty
import sys
from typing import IO


class Buffering:

    def __init__(self, file: IO):
        self.fd = file.fileno()
        self.file = file
        self.settings = termios.tcgetattr(file)

    def on(self) -> None:
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.settings)

    def off(self) -> None:
        tty.setcbreak(self.file)

    def __enter__(self, *args) -> None:
        self.off()

    def __exit__(self, *args) -> None:
        self.on()


buffering = Buffering(sys.stdin)
