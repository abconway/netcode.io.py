from pysodium import (
    crypto_aead_chacha20poly1305_ietf_encrypt,
    crypto_aead_chacha20poly1305_ietf_decrypt,
    crypto_aead_chacha20poly1305_ietf_NONCEBYTES,
)


def pad(msg, length, pad_char, front=True):
    if type(msg) != type(pad_char):
        raise TypeError(
            'Input "{}" (type: {}) not the same type as pad "{}" (type: {})'
            .format(msg, type(msg), pad, type(pad))
        )

    current_length = len(msg)
    diff = length - current_length

    if diff == 0:
        return msg

    if diff < 0:
        raise ValueError(
            'Padded length of {} cannot be shorter than msg length of "{}" ({})'
            .format(length, msg, len(msg))
        )

    if front:
        return (pad_char * diff) + msg
    return msg + (pad_char * diff)


def encrypt(msg, nonce, key, ad=None):
    if type(msg) != bytes:
        msg = bytes(msg, encoding='utf-8')
    if type(nonce) != bytes:
        nonce = bytes(
            pad(str(nonce), length=crypto_aead_chacha20poly1305_ietf_NONCEBYTES, pad_char='0'),
            encoding='utf-8',
        )
    if ad and type(ad) != bytes:
        ad = bytes(ad, encoding='utf-8')
    return crypto_aead_chacha20poly1305_ietf_encrypt(msg, ad, nonce, key)


def decrypt(msg, nonce, key, ad=None):
    if type(nonce) != bytes:
        nonce = bytes(
            pad(str(nonce), length=crypto_aead_chacha20poly1305_ietf_NONCEBYTES, pad_char='0'),
            encoding='utf-8',
        )
    if ad and type(ad) != bytes:
        ad = bytes(ad, encoding='utf-8')
    return crypto_aead_chacha20poly1305_ietf_decrypt(msg, ad, nonce, key)
