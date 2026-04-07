import platform

if platform.system() == "Windows":
    from .windows import getkey
else:
    from .unix import getkey
