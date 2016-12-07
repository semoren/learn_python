#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        # 获取锁:
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁:
            lock.release()

t1 = threading.Thread(target=change_it, args=(5,))
t2 = threading.Thread(target=change_it, args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print(balance)