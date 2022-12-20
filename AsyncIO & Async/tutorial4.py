import asyncio, random, time


async def foo():
    await asyncio.sleep(random.randint(1, 8) / 10.0)
    end = time.time()
    print(f"foo()耗时{end - start}秒")
    return 101


async def foo2():
    await asyncio.sleep(random.randint(1, 8) / 10.0)
    end = time.time()
    print(f"foo2()耗时{end - start}秒")
    return 102


async def foo3():
    await asyncio.sleep(random.randint(1, 8) / 10.0)
    end = time.time()
    print(f"foo3()耗时{end - start}秒")
    return 103


async def main():
    R = [foo(), foo2(), foo3()]
    await asyncio.gather(*R)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())

    end = time.time()
    print(f"__main__耗时{end - start}秒")
