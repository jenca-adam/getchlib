try:
    from .getkey import getkey
except:
    from getkey import getkey
import sys
class module:
    def get_pressed(self):
        return list(getkey(False,0.01))
    pressed=property(get_pressed)
sys.modules[__name__]=module()
