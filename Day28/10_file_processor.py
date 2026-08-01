# File Processor using Threads

import threading
import time

def process(filename):
    print("Processing", filename)
    time.sleep(2)
    print(filename, "Completed")

files = [
    "report.pdf",
    "notes.txt",
    "image.png"
]

threads = []

for file in files:
    thread = threading.Thread(target=process, args=(file,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("All files processed.")
