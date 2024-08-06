#!/usr/bin/env python3
'''writing the coroutine'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''return the list of float number between 0 and 10'''
    for _ in range(10):
        num = random.random() * 10
        await asyncio.sleep(1)
        yield num
