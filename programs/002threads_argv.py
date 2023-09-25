import threading
import time


taolist=[]
def count(n):
    for i in range(1,n+1):
        print(i)
        taolist.append(i)
        time.sleep(0.8)

def count2(n):
    for i in range(1,n+1):
        print(i)
        taolist.append(i)
        time.sleep(2) 

# for _ in range(3):
#     x= threading.Thread(target=count,args=(5,))
#     x.start()

x= threading.Thread(target=count,args=(5,))
x.start()
y= threading.Thread(target=count2,args=(5,))
y.start()

print("Done")
# time.sleep(12)
x.join()
y.join()

print(taolist)