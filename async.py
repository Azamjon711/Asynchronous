import asyncio
from datetime import datetime


async def task_1():
    await asyncio.sleep(3)
    print("Task 1")


async def task_2():
    await asyncio.sleep(2)
    print("Task 2")


async def task_3():
    await asyncio.sleep(7)
    print("Task 3")


async def task_4():
    await asyncio.sleep(4)
    print("Task 4")


async def main():
    await asyncio.gather(task_4(), task_3(), task_1(), task_2())


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())
