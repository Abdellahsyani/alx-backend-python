#!/usr/bin/env python3
'''return the list af the delays'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''a function that return the list of list of all delay'''
    delay_list = []
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delay_list.extend(delays)
    for i in range(len(delay_list)):
        key = delay_list[i]
        j = i - 1
        while j >= 0 and key < delay_list[j]:
            delay_list[j + 1] = delay_list[j]
            j -= 1
        delay_list[j + 1] = key
    return delay_list
