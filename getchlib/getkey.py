import platform
import sys
if platform.system()=='Windows':
    try:
        from . import windows
    except ImportError:
        import windows
    module=windows
else:
    try:
        from . import unix
    except ImportError:
        import unix
    module=unix
sys.modules[__name__]=unix
