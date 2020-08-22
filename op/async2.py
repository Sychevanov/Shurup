import asyncio
async def character1():
    for i in range(0,4,2):
        print(f'def_char1 {i}')
        await asyncio.sleep(0)

async def character2():
    for j in range(1,4,2):
        print(f'def_char2 {j}')
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
tasks = [loop.create_task(character1()), loop.create_task(character2())]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)
loop.close()