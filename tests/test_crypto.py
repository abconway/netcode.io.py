import pytest
from pysodium import (
    crypto_aead_chacha20poly1305_ietf_KEYBYTES,
)

from netcode.crypto import (
    encrypt,
    decrypt,
    pad,
)


@pytest.mark.parametrize('input,length,pad_char,front,expected', [
    ('1234', 5, '0', True, '01234'),
    ('1234', 8, 'x', False, '1234xxxx'),
    (b'1234', 6, b'\xee', True, b'\xee\xee1234'),
    (b'1234', 4, b'\xee', True, b'1234'),
])
def test_pad(input, length, pad_char, front, expected):
    assert pad(input, length, pad_char, front) == expected


def test_pad_exceptions():
    with pytest.raises(TypeError):
        pad(b'1234', 8, '0')

    with pytest.raises(ValueError):
        pad('123456789', 4, '0')


def test_encrypt_decrypt():
    KEY = bytes(
        pad(
            'ThisIsASuperSecretKey',
            length=crypto_aead_chacha20poly1305_ietf_KEYBYTES,
            pad_char='0',
        ),
        encoding='utf-8',
    )
    message = 'Hello world!'
    associated_data = b'1bn23rlvk1jb3lk1345'
    encrypted = encrypt(message, nonce=1, key=KEY, ad=associated_data)
    decrypted = decrypt(encrypted, nonce=1, key=KEY, ad=associated_data)
    assert message == decrypted.decode('utf-8')
