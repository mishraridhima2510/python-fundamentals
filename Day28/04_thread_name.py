# Thread Name

import threading

def show():
    print(threading.current_thread().name)

thread = threading.Thread(target=show, name="Worker")

thread.start()
thread.join()
