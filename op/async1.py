import asyncio
async def character1():
    for i in range(0,4,2):
        print(f'def_char1 {i}')
        await asyncio.sleep(0)

async def character2():
    for j in range(1,4,2):
        print(f'def_char2 {j}')
        await asyncio.sleep(0)

async def game():
    task1 = asyncio.create_task(character1())
    task2 = asyncio.create_task(character2())
    
    await asyncio.gather(task1,task2)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(game())
loop.close()
#asyncio.run(game())