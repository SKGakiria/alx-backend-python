#!/usr/bin/env python3
"""Module containing a async routine that spawns wait_random n times
with specified delay calls"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function returns sorted list of delays"""
    l_tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(l_tasks)]
