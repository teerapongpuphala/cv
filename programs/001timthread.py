import threading
import time

def func():
    print('run')
    time.sleep(3)
    print("done")

x = threading.Thread(target=func)
x.start()

print(threading.activeCount())
time.sleep(4)
print("s")