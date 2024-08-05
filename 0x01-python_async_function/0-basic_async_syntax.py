#!/usr/bin/env python3
'''generating a float number number'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''write an asynchronous coroutine'''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
