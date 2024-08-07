#!/usr/bin/env python3
'''start the functon'''
import asyncio
import time


async_comprehension = __import__('user').async_comprehension


async def measure_runtime() -> float:
    '''return the total time that the parallel take to run'''
    start_time = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return time.time() - start_time
