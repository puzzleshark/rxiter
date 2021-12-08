# RxIter

RxIter brings observables to python in a bare bones way by using **async generators** and the *async* *await* syntax. In this paradigm **observables** are analgous to **async iterables**, and **observers** analogous to **async iterators**.


It implements 2 fundamental observable operations, which may be familar to those who know **rxpy**.

* [**share**](#Share)
* [**repeat**](#Repeat)

## Installation
```
pip install git+https://github.com/puzzleshark/rxiter
```

## Operations

### Share
`share` allows multiple "observers" to subscribe the same observable
```
@share
async count():  # a counting "observable"
  count = 0
  while True:
    yield count
    await asyncio.sleep(1)
    count += 1

async count_squared():
  async for c in count():  # subscribe to `count` by async iterating on it
    print(f"{c} squared is {c**2})
square_task_subscription = asyncio.Task(count_squared())

async count_cubed():
  async for c in count():
    print(f"{c} cubed is {c**3}")
cube_task_subscripton = asyncio.Task(count_cubed())
```
### Repeat
`repeat` takes a **iterator**, and "records" it's outputed values so that it is turned into an **iterable**, and can be "listened" back multiple times.

## Example
Suppose we have a api endpoint that we would like to poll to get the most up to for let's say the weather in Toronto. We could set up an observable as follows:

```
async get_toronto_weather():
  while True:
    yield await poll_my_api("api_enpoint") 
```

If you want to "pipe" this to do further operations, like extract some specific content from the dict returned by `get_toronto_weather()`

```
async get_temperature():
  async for v in poll_api():
    yield v["temperature"]
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

