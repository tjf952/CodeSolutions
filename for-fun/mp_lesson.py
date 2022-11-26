#!/usr/bin/env python3

"""Multiprocessing Workshop 1

Shows time calculations

Usage: $ python3 m.py
"""

import concurrent.futures
import multiprocessing
import time


def foobar(seconds: int) -> None:
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")

def foobar2(seconds: int) -> None:
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} seconds(s)..."

def mp_generic() -> None:
    p1 = multiprocessing.Process(target=foobar)
    p1.start()
    p1.join()

def mp_generic() -> None:
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=foobar, args=[1.5])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

def mp_pool() -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = [executor.submit(foobar2, sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

def mp_pool2() -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5,4,3,2,1]
        results = executor.map(foobar2, secs)
        for result in results:
            print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    mp_pool2()
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} second(s)")
