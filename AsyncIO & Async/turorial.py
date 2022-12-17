import asyncio


async def main():
    print("elden ring")
    task = asyncio.create_task(foo('text'))
    print('finished')


async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())
