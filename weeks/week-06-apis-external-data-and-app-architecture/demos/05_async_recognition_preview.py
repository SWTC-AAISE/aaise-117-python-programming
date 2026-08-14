"""
Week 6 Demo 5: async recognition preview

Purpose:
Give recognition-level exposure to asynchronous Python without turning it
into a full unit.
"""

import asyncio


async def fetch_message():
    await asyncio.sleep(0)
    return "Simulated async result ready."


async def main():
    message = await fetch_message()
    print(message)


asyncio.run(main())

