import asyncio
from contextvars import ContextVar, Context

var_what = ContextVar("what")


async def hello():
    try:
        return f"Variable from context: {var_what.get()}"
    except LookupError:
        return "No such variable"


async def _f():
    assert await hello() == "No such variable"
    task_1 = asyncio.create_task(hello())
    coroutine_1 = hello()
    var_what.set("I will appear only on task 2")
    task_2 = asyncio.create_task(hello())
    coroutine_2 = hello()
    assert await task_1 == "No such variable"
    assert await task_2 == "Variable from context: I will appear only on task 2"
    assert await coroutine_1 == "Variable from context: I will appear only on task 2"
    assert await coroutine_2 == "Variable from context: I will appear only on task 2"


if __name__ == '__main__':
    asyncio.run(_f())
