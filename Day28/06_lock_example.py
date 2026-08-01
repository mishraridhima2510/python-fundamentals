# Lock Example

import threading

lock = threading.Lock()

def display():
    with lock:
        print("Resource Locked")

thread1 = threading.Thread(target=display)
thread2 = threading.Thread(target=display)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
