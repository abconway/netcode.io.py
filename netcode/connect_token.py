from .fields import Field


UINT64_BYTES = 8
UINT32_BYTES = 4
UINT16_BYTES = 2
UINT8_BYTES = 1

VERSION_INFO_BYTES = 13
PROTOCOL_ID_BYTES = UINT64_BYTES
CREATE_TIMESTAMP_BYTES = UINT64_BYTES
EXPIRE_TIMESTAMP_BYTES = UINT64_BYTES
SEQUENCE_BYTES = UINT64_BYTES
PRIVATE_BYTES = 1024
TIMEOUT_SECONDS_BYTES = UINT32_BYTES
NUM_SERVER_ADDRESSES_BYTES = UINT32_BYTES


CLIENT_TO_SERVER_KEY_BYTES = 32
SERVER_TO_CLIENT_KEY_BYTES = 32
USER_DATA_BYTES = 256
NONCE_BYTES = 24
CONNECT_TOKEN_BYTES = 2048
SERVER_ADDRESS_IPV4_BYTES = 7
SERVER_ADDRESS_IPV6_BYTES = 19


class ConnectToken:

    def __init__(self):
        self.fields = [
            Field('version_info', VERSION_INFO_BYTES, 'string'),
            Field('protocol_id', PROTOCOL_ID_BYTES, 'int'),
            Field('create_timestamp', CREATE_TIMESTAMP_BYTES, 'int'),
            Field('expire_timestamp', EXPIRE_TIMESTAMP_BYTES, 'int'),
            Field('sequence', SEQUENCE_BYTES, 'int'),
            Field('private', PRIVATE_BYTES, 'int'),
            Field('timeout_seconds', TIMEOUT_SECONDS_BYTES, 'int'),
            Field('num_server_addresses', NUM_SERVER_ADDRESSES_BYTES, 'int'),
        ]


ADDRESS_TYPE_BYTES = UINT8_BYTES
IPV4_ADDRESS_PART_BYTES = UINT8_BYTES
IPV6_ADDRESS_PART_BYTES = UINT16_BYTES
PORT_BYTES = UINT16_BYTES


class ServerAddressIPV4:

    def __init__(self):
        self.fields = [
            Field('address_type', ADDRESS_TYPE_BYTES, 'int'),
            Field('a', IPV4_ADDRESS_PART_BYTES, 'int'),
            Field('b', IPV4_ADDRESS_PART_BYTES, 'int'),
            Field('c', IPV4_ADDRESS_PART_BYTES, 'int'),
            Field('d', IPV4_ADDRESS_PART_BYTES, 'int'),
            Field('port', PORT_BYTES, 'int'),
        ]


class ServerAddressIPV6:

    def __init__(self):
        self.fields = [
            Field('address_type', ADDRESS_TYPE_BYTES, 'int'),
            Field('a', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('b', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('c', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('d', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('e', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('f', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('g', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('h', IPV6_ADDRESS_PART_BYTES, 'int'),
            Field('port', PORT_BYTES, 'int'),
        ]