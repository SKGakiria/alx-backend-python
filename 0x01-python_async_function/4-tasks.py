#!/usr/bin/env python3
"""Module containing function that performs the asynchronous tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function returns the sorted list of delays"""
    l_tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(l_tasks)]
