# Parallel Download Simulation

import threading
import time

def download(file):
    print(file, "Downloading...")
    time.sleep(2)
    print(file, "Completed")

files = ["File1", "File2", "File3"]

threads = []

for file in files:
    thread = threading.Thread(target=download, args=(file,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
