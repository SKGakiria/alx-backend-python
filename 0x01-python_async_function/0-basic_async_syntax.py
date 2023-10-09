#!/usr/bin/env python3
"""Module containing an asynchronous coroutine that generates random delays"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Function that generates random delays and prints it"""
    rand_delay = random.uniform(0, max_delay)
    await asyncio.sleep(rand_delay)
    return rand_delay
