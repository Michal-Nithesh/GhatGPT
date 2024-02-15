from websockets import serve
from asyncio import run

async def echo(ws):
    async for m in ws:
        print(f'Mike: {m}')
        await ws.send(input('Me: '))

async def main():
    s = await serve(echo, 'localhost', 5000)
    await s.serve_forever()

run(main())
