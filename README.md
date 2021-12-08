# RxIter

RxIter brings observables to python in a bare bones way by using **async generators** and the *async* *await* syntax. In this paradigm **observables** are analgous to **async iterables**, and **observers** analogous to **async iterators**.


It implements 2 fundamental core operations, which may be familar to those who know **rxpy**.

* **share**
* **repeat**

## Installation
```
pip install git+https://github.com/puzzleshark/rxiter
```

## Operations

### Share
`share` allows multiple "observers" to subscribe the same observable
```
@share
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

asyncio.Task(count_squared())
asyncio.Task(count_cubed())
```
### Repeat
`repeat` takes a iterator, and "records" it's outputed values to be listened to by multiple observers.

## Example

A simple "counting" observable might be implemented as

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

Now if we want to have multiple listeners, that is where the `share` comes into the picture. We can do

```
@share
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

asyncio.Task(count_squared())
asyncio.Task(count_cubed())
```

and `count()` will only run once for both `count_squared()` and `count_cubed()`

