# Thread Join

import threading
import time

def work():
    time.sleep(2)
    print("Work Finished")

thread = threading.Thread(target=work)

thread.start()
thread.join()

print("Main Program Finished")
