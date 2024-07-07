import getchlib
import time
a=getchlib.HotKeyListener(blocking=False)
a.add_hotkey('a',lambda:print("hello"))
a.start()
print("Press a to print hello")
e=0
while True:
    print("loop",e)
    
    time.sleep(1)
    e+=1
    if e==5:
        print("not anymore:(")
        a.terminate()
