import platform
import sys
if platform.system()=='Windows':
    from . import windows
    module=windows
else:
    from . import unix
    module=unix
sys.modules[__name__]=module
