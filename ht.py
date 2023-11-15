import getchlib
import time
a=getchlib.HotKeyListener(blocking=False)
a.add_hotkey('a',lambda:print("hello"))
a.start()
print("Press a to print hello")
while True:
    print("loop")
    time.sleep(1)
