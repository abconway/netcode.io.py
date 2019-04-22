import asyncio
import base64

import requests

from netcode.crypto import encrypt, decrypt, KEY


UINT64_BYTES = 8
UINT32_BYTES = 4
UINT16_BYTES = 2
UINT8_BYTES = 1
CLIENT_TO_SERVER_KEY_BYTES = 32
SERVER_TO_CLIENT_KEY_BYTES = 32
USER_DATA_BYTES = 256
CONNECT_TOKEN_PRIVATE_BYTES = 1024
VERSION_INFO_BYTES = 13
SEQUENCE_BYTES = 8
NONCE_BYTES = 24
CONNECT_TOKEN_BYTES = 2048
SERVER_ADDRESS_IPV4_BYTES = 7
SERVER_ADDRESS_IPV6_BYTES = 19

CONNECT_TOKEN = [
    'version_info',
    'protocol_id',
    'create_timestamp',
    'expire_timestamp',
    'connect_token_sequence',
    'connect_token_private',
    'timeout_seconds',
    'num_server_addresses',
    'server_address_ipv4',
    'server_address_ipv6',
    'client_to_server_key',
    'server_to_client_key',
]

SERVER_ADDRESS_IPV4 = [
    'address_type',
    'a',
    'b',
    'c',
    'd',
    'port'
]

SERVER_ADDRESS_IPV6 = [
    'address_type',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'port',
]

SIZE_BYTES = {
    'version_info': VERSION_INFO_BYTES,
    'protocol_id': UINT64_BYTES,
    'create_timestamp': UINT64_BYTES,
    'expire_timestamp': UINT64_BYTES,
    'connect_token_nonce': NONCE_BYTES,
    'connect_token_sequence': SEQUENCE_BYTES,
    'connect_token_private': CONNECT_TOKEN_PRIVATE_BYTES,
    'timeout_seconds': UINT32_BYTES,
    'num_server_addresses': UINT32_BYTES,
    'server_address_ipv4': SERVER_ADDRESS_IPV4_BYTES,
    'server_address_ipv6': SERVER_ADDRESS_IPV6_BYTES,
    'client_to_server_key': CLIENT_TO_SERVER_KEY_BYTES,
    'server_to_client_key': SERVER_TO_CLIENT_KEY_BYTES,
    'address_type': UINT8_BYTES,
    'a': UINT8_BYTES,
    'b': UINT8_BYTES,
    'c': UINT8_BYTES,
    'd': UINT8_BYTES,
    'e': UINT16_BYTES,
    'f': UINT16_BYTES,
    'g': UINT16_BYTES,
    'h': UINT16_BYTES,
    'i': UINT16_BYTES,
    'j': UINT16_BYTES,
    'k': UINT16_BYTES,
    'l': UINT16_BYTES,
    'port': UINT16_BYTES,
}


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


if __name__ == '__main__':
    resp = requests.get('http://localhost:8880/token')
    json_resp = resp.json()
    token_bytes = base64.b64decode(json_resp.get('connect_token'))
    print(token_bytes)
    for field in CONNECT_TOKEN:
        size = SIZE_BYTES[field]
        value = token_bytes[:size]
        token_bytes = token_bytes[size:]
        print(field)
        print(value)
        try:
            print(str(int.from_bytes(value, byteorder='little')))
        except Exception as e:
            print(e)



# async def main():
#     # Get a reference to the event loop as we plan to use
#     # low-level APIs.
#     loop = asyncio.get_running_loop()
#
#     message = "Hello World!"
#     transport, protocol = await loop.create_datagram_endpoint(
#         lambda: ClientProtocol(message, loop),
#         remote_addr=('127.0.0.1', 9999))
#
#     try:
#         await protocol.on_con_lost
#     finally:
#         transport.close()
#
#
# asyncio.run(main())
