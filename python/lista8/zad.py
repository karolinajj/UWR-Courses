#Karolina Jędraszek
#lista 8

import requests
import asyncio
import aiohttp
from aiohttp import ClientSession

from prywatne import KEY #additional file with keys


async def download_API(url,host, params):

    headers = {
        "X-RapidAPI-Key": KEY,
        "X-RapidAPI-Host": host
    }
    async with aiohttp.ClientSession() as session:
            async with session.get(url, headers = headers, params = params) as response:
                res = await response.json()
    return res

#data:
urls = [("https://booking-com15.p.rapidapi.com/api/v1/meta/getLanguages",
        "booking-com15.p.rapidapi.com", {}),
        ("https://weatherbit-v1-mashape.p.rapidapi.com/forecast/minutely",
         "weatherbit-v1-mashape.p.rapidapi.com", {"lat":"35.5","lon":"-78.5"})]

async def main():
    async with aiohttp.ClientSession() as session:
        requests = [download_API(url, host, params) for url, host, params in urls]
        pages = await asyncio.gather(*requests)
        print(pages)

asyncio.run(main())