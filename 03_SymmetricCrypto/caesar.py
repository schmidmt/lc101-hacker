#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Caesar Cipher Tools"""


def shift(ch, k):
    if ch.isalpha():
        return chr(((ord(ch.lower()) + k - ord('a')) % 26) + ord('a'))
    return ch


def encrypt(raw_text, key):
    """Encypt raw_text using the Caesar cipher.

    Arguments:
        raw_text [str] - String to encrypt
        key [int] - Key Code
    """
    out = ''
    for ch in raw_text:
        out += shift(ch, key)
    return out


def decrypt(raw_text, key):
    """Decrypt raw_text using the Caesar cipher.

    Arguments:
        raw_text [str] - String to decrypt
        key [int] - Key Code
    """
    out = ''
    for ch in raw_text:
        out += shift(ch, -key)
    return out


def list_possible(enc_text):
    """List possible solutions
    """

    for i in range(26):
        print(i, decrypt(enc_text, i))


def main():
    enc_text = input('Encrypted: ')
    list_possible(enc_text)


if __name__ == "__main__":
    main()
