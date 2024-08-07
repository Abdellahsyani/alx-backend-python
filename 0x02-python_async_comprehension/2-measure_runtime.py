#!/usr/bin/env python3
'''start the functon'''
import asyncio
import time


async_comprehension = __import__('user').async_comprehension


async def measure_runtime():
    '''return the total time that the parallel take to run'''
    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    result = await asyncio.gather(*tasks)

    return time.time() - start_time
