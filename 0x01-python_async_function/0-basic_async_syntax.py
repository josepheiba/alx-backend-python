#!/usr/bin/env python3
"""Asyncio testing."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return it."""
    ranum = random.uniform(0, max_delay)
    await asyncio.sleep(ranum)
    return ranum
