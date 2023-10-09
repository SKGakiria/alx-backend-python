#!/usr/bin/env python3
"""Module containing function with corouting that loops 10 times"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function returns a yield of random numbers between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
