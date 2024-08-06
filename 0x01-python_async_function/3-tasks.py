#!/usr/bin/env python3
'''Just a regular fucntion'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''return the object'''
    obj = asyncio.create_task(wait_random(max_delay))
    return obj
