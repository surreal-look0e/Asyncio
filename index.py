# Asynchronous Web Scraping with Asyncio
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://example.com'
    html = await fetch(url)
    print(html)

asyncio.run(main())
