#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio,threading

@asyncio.coroutine
def hello():
    print('Hello word! (%s)' % threading.current_thread())
    # 异步调用asyncio.sleep(1)
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())


# 获取EventLoop
loop = asyncio.get_event_loop()

tasks=[hello(), hello()]

# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()