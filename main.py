'''the top level script'''
import asyncio

def run_client(listen_only=None) -> None:
    '''runs the client with (possibly) specified arguments'''
    client = __import__('client')
    if listen_only is not None:
        client.main(listen_only=listen_only)
    else:
        client.main()

async def run_server():
    '''runs bundled server (dev feature, not to be included in final product)'''
    server = __import__('server')
    server.start()


async def main_with_server():
    '''Different enough to seperate into it's own function. Runs the server, followed by the client. Good for unit tests.'''
    server = asyncio.create_task(asyncio.to_thread(lambda: asyncio.run(run_server())))
    await asyncio.sleep(2)
    await run_client()
    await server

async def main():
    '''manages all functions, similar to a C-style main'''
    listener = asyncio.create_task(asyncio.to_thread(run_client, True,))
    await run_client(False)
    await listener

if __name__ == '__main__':
    asyncio.run(main())

