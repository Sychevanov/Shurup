import asyncio
async def character1():
    for i in range(2):
        print(f'def_char1 {i}')
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.run_until_complete(character1())
loop.close()