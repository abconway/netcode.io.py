import asyncio

from netcode.crypto import encrypt, decrypt, KEY


class ClientProtocol:
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop
        self.transport = None
        self.on_con_lost = loop.create_future()

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(encrypt(self.message, nonce=1, key=KEY))

    def datagram_received(self, data, addr):
        print("Received:", decrypt(data, nonce=1, key=KEY))

        print('Send:', self.message)
        self.transport.sendto(encrypt(self.message, nonce=1, key=KEY))

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Connection closed")
        self.on_con_lost.set_result(True)


async def main():
    # Get a reference to the event loop as we plan to use
    # low-level APIs.
    loop = asyncio.get_running_loop()

    message = "Hello World!"
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientProtocol(message, loop),
        remote_addr=('127.0.0.1', 9999))

    try:
        await protocol.on_con_lost
    finally:
        transport.close()


asyncio.run(main())
