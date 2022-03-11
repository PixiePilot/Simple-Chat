import asyncio
import time

async def run_client():
    print('1')
    client = __import__('client')
    print('2')
    client.main()
    print('3')

async def run_server():
    server = __import__('server')
    server.main()

async def main():
    server = asyncio.create_task(asyncio.to_thread(lambda: asyncio.run(run_server())))
    await asyncio.sleep(2)
    print('running client')
    await run_client()
    await server

asyncio.run(main())
