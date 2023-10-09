#!/usr/bin/env python3
"""Module containing function that takes an integer max_delay"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function takes an integer and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
