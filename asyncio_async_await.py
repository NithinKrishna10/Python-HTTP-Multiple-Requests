import asyncio


async def main():
    # await asyncio.sleep(5)
    print('nithin')
    await nice("blaze")

async def nice(text):
    print(text)
    await asyncio.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.gather(main(),nice("hai"))
    # print(type(main()))
