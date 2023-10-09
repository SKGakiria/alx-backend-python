#!/usr/bin/env python3
"""Module containing function that measures the total
execution time for wait_n"""
import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function returns the average time per call by dividing
    the total elapsed time by n"""
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = perf_counter() - start
    return elapsed_time / n
