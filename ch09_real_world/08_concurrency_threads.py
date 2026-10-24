"""9.8 Doing several things at once with threads.

Real-world comparison: a restaurant kitchen. One cook making 5 dishes
one after another is slow, mostly because of waiting for things to
boil. Five cooks can wait at the same time. Threads help most when a
program spends its time WAITING (for downloads, files, databases).
"""

import time
from concurrent.futures import ThreadPoolExecutor


def download(page):
    time.sleep(0.3)                # pretend to wait for the network
    return f"{page} ({len(page) * 100} bytes)"


pages = ["home", "about", "pricing", "blog", "contact"]

start = time.perf_counter()
results = [download(p) for p in pages]
one_by_one = time.perf_counter() - start
print(f"One at a time: {one_by_one:.2f} s")

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(download, pages))
together = time.perf_counter() - start
print(f"With 5 threads: {together:.2f} s")
print("Results:", results)
print(f"About {one_by_one / together:.0f}x faster")

# Shared data needs a Lock so two threads do not write at once.
import threading

counter = 0
lock = threading.Lock()


def add_visits(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


threads = [threading.Thread(target=add_visits, args=(10_000,)) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("Visits counted:", counter)

# For heavy maths (not waiting), use multiprocessing or
# ProcessPoolExecutor to use several CPU cores instead.
