#!/usr/bin/env python3

import asyncio


measure_runtime = __import__('1-test').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
