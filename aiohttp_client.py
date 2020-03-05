import aiohttp
import asyncio

async def fetch(session, url):
    async with session.post(url,'["data"]') as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://localhost:8080')
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())