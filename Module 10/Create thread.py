import time
from threading import Thread


def digits():
    for i in range(1, 11):
        time.sleep(1)
        print(i)


def letters():
    for i in range(ord('a'),ord('j')+1):
        time.sleep(1)
        print(chr(i))


thread1 = Thread(target=digits)
thread2 = Thread(target=letters)
thread1.start()
time.sleep(0.1)
thread2.start()
thread1.join()
thread2.join()
