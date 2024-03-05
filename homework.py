import asyncio
import json
from datetime import datetime


async def task1():
    with open("data1.json", "r") as file1:
        data = json.load(file1)

        print("Task 1")

        names = []
        prices = []

        for i in data["course"]:
            names.append(i["name"])
            prices.append(i["price"])

    with open("data2.json", "w") as file2:
        json.dump(names, file2, indent=4)
        json.dump(prices, file2, indent=5)


async def main():
    await asyncio.gather(task1())


if __name__ == "__main__":
    print(datetime.now().time())
    asyncio.run(main())
    print(datetime.now().time())