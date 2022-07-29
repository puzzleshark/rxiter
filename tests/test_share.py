import asyncio

from rxiter import share

async def test_basic_share():
    """
    Test that when two observables depend on one, the first one is not executed twice.
    """

    total = []

    @share
    async def count():
        v = 0
        while True:
            yield v
            total.append(v)
            await asyncio.sleep(1)
            v += 1

    async def count_squared():
        async for v in count():
            yield v ** 2

    async def count_cubed():
        async for v in count():
            yield v ** 3
    
    square_iter = count_squared()
    cube_iter = count_cubed()
    for i in range(10):
        s = await anext(square_iter)
        c = await anext(cube_iter)
    
    assert len(total) == 10

