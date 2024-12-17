import asyncio
from websockets.asyncio.server import serve


CONNECTED_CLIENTS = set()


async def echo(websocket):
    CONNECTED_CLIENTS.add(websocket)
    print(f"new connection. [{len(CONNECTED_CLIENTS)}]")
    try:
        message = await websocket.recv()
        print(f"Message recieved: {message}")
        if CONNECTED_CLIENTS:
            await asyncio.wait([client.send(message) for client in CONNECTED_CLIENTS])
    except:
        pass
    finally:
        CONNECTED_CLIENTS.remove(websocket)
        print(f"connection closed. [{len(CONNECTED_CLIENTS)}]")


async def main():
    async with serve(echo, "0.0.0.0", 8765) as server:
        print("server running.")
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())