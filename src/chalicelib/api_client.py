import aiohttp
import asyncio
import json
from src import config 

async def postapi(headers, url, data):
    """
    Send an HTTP POST
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
            result = await resp.json()
    return result, resp.status


async def getapi(headers, url):
    """
    Send an HTTP GET
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            result = await resp.json()
    return result, resp.status