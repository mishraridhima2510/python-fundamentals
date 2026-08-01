# Thread Basics

import threading

def task():
    print("Thread is running")

thread = threading.Thread(target=task)

thread.start()
thread.join()
