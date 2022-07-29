import asyncio

from rxiter import share

class TestShare:

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
                yield v ** 2

        async def count_cubed():
            async for v in count():
                yield v ** 3
        
        for i in range(10):
            squares = aiter(count_squared())
            cubes = aiter(count_cubed())
            s = await anext(squares)
            await anext(cubes)