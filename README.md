# RxIter

RxIter brings observables to python in a bare bones way by using **async generators** and the *async* *await* syntax. In this paradigm **observables** are analogous to **async iterables**, and **observers** analogous to **async iterators**.


It implements 2 fundamental observable operations, which may be familar to those who know **rxpy**.

* [**share**](#Share)
* [**repeat**](#Repeat)

## Operations

### Share
`share` allows multiple "observers" to subscribe the same observable
```
@share
async count():  # a counting "observable"
  v = 0
  while True:
    yield v
    await asyncio.sleep(1)
    v += 1

async count_squared(obs):  # a counting "observer"
  async for v in obs: 
    print(f"{v} squared is {v**2})

square_task_subscription = asyncio.Task(count_squared(count()))  # subscribe

async count_cubed(obs):  # another counting "observer
  async for v in obs:
    print(f"{v} cubed is {v**3}")

cube_task_subscripton = asyncio.Task(count_cubed(count())). # subscribe
```
### Repeat
`repeat` takes a **iterator**, and "records" it's outputed values so that it is turned into an **iterable**, and can be "listened" back multiple times.

## Example
Suppose we have a API endpoint that we would like to poll to get the most up to date weather in Toronto. We could set up an observable as follows:

```
async get_toronto_weather():
  while True:
    yield await poll_my_api("api_enpoint")
    await asyncio.sleep(60 * 30)  # wait 30 minutes
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
async get_toronto_weather():
  while True:
    yield await poll_my_api("api_enpoint")
    await asyncio.sleep(60 * 30)  # wait 30 minutes

async get_temperature():
  async for v in poll_api():
    yield v["temperature"]

async get_humidity():
  async for v in poll_api():
    yield v["humidity"]

asyncio.Task(count_squared())
asyncio.Task(count_cubed())
```

and `count()` will only run once for both `count_squared()` and `count_cubed()`

## Installation
```
pip install git+https://github.com/puzzleshark/rxiter
```
