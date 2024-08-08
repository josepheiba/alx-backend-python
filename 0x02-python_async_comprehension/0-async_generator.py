#!/usr/bin/env python3
"""Asyncio Generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Wait for a random delay and return it."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
