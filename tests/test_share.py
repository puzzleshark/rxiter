import asyncio

from rxiter import share

async def test_basic_share():
    print("what")

    @share
    async def count():
        v = 0
        while True:
            print(f"returning value {v}")
            yield v
            await asyncio.sleep(1)
            v += 1

    async def count_squared():
        async for v in count():
            print(f"{v} squared is {v**2}")
            yield v ** 2

    async for c in count_squared():
        print(c)
        if c > 10:
            break


asyncio.run(test_basic_share())