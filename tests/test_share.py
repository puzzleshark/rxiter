import asyncio

from rxiter import share

async def test_basic_share():
    print("what")

    @share
    async def count():
        c = 0
        while True:
            yield c
            await asyncio.sleep(1)
            c += 1

    async def count_squared():
        async for c in count():
            yield c ** 2

    async for c in count_squared():
        print(c)
        if c > 10:
            continue
