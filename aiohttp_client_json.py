import asyncio
import aiohttp

async def fetch(session):
    print('Query http://localhost:8080')
    async with session.post('http://localhost:8080', data=b'data') as resp:
        print(resp)



async def go():
    async with aiohttp.ClientSession() as session:
        await fetch(session)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()