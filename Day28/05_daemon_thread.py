# Daemon Thread

import threading
import time

def background():
    while True:
        print("Running...")
        time.sleep(1)

thread = threading.Thread(target=background, daemon=True)

thread.start()

time.sleep(3)

print("Main Program Ended")
