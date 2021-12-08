# RxIter

RxIter tries to bring observables to python in a bare bones way by using async generators and the `async` `await` syntax. In this paradigm observables are analgous to async iterables, and observers are analogous to async iterators. A simple "counting" observable might be implemented as

```
async count():
  count = 0
  while True:
    yield count
    await asyncio.sleep(1)
    count += 1
```

If you want to "pipe" this to do further operations, you might do something like

```
async count_squared():
  async for c in count():
    yield c**2
```

Now if we want to have multiple listeners, that is where the `async_share_dec` comes into the picture. We can do

```
@async_share_dec
async count():
  count = 0
  while True:
    yield count
    await asyncio.sleep(1)
    count += 1

async count_squared():
  async for c in count():
    yield c**2

async count_cubed():
  async for c in count():
    yield c**3
```

It implements 2 fundamental core operations

* `async_share_dec`
* `async_repeat_dec`

`async_share_dec` is a function to decorate an async generator.
