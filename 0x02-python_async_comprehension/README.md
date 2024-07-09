Asynchronous Comprehensions

```
# example of an asynchronous list comprehension with an generator
import asyncio
 
# define an asynchronous generator
async def async_generator():
    # normal loop
    for i in range(10):
        # block to simulate doing work
        await asyncio.sleep(1)
        # yield the result
        yield i
 
# main coroutine
async def main():
    # asynchronous list comprehension
    results = [item async for item in async_generator()]
    # report results
    print(results)
 
# start the asyncio program
asyncio.run(main())


# example of an asynchronous list comprehension with an iterator
import asyncio
 
# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0
 
    # create an instance of the iterator
    def __aiter__(self):
        return self
 
    # return the next awaitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # block to simulate work
        await asyncio.sleep(1)
        # increment the counter
        self.counter += 1
        # return the counter value
        return self.counter
 
# main coroutine
async def main():
    # asynchronous list comprehension
    results = [item async for item in AsyncIterator()]
    # report results
    print(results)
 
# start the asyncio program
asyncio.run(main())


# example of an await list comprehension
import asyncio
 
# task coroutine
async def task_coro(value):
    # block a moment to simulate work
    await asyncio.sleep(1)
    # calculate and return
    return value * 10
 
# main coroutine
async def main():
    # create a list of awaitables
    awaitables = [task_coro(i) for i in range(10)]
    # await list comprehension to collect results
    results = [await a for a in awaitables]
    # report results
    print(results)
 
# run the asyncio program
asyncio.run(main())
```
