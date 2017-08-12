#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Vigenere Cipher Tools"""


def shift(ch, k):
    if ch.isalpha():
        return chr(((ord(ch.lower()) + k - ord('a')) % 26) + ord('a'))
    return ch


def encrypt(raw_text, key):
    """Encypt raw_text using the Vigenere cipher.

    Arguments:
        raw_text [str] - String to encrypt
        key [str] - Key string
    """
    out = ''
    keylen = len(key)
    keynums = [ord(k.lower()) - ord('a') for k in key]
    for i, ch in enumerate(raw_text):
        out += shift(ch, keynums[i % keylen])
    return out


def decrypt(raw_text, key):
    """Decrypt Vigenere encrypted text"""
    out = ''
    keylen = len(key)
    keynums = [ord(k.lower()) - ord('a') for k in key]
    for i, ch in enumerate(raw_text):
        out += shift(ch, -keynums[i % keylen])
    return out


def main():
    plain_text = input('Plain Text: ')
    key = input('Key: ')

    print(encrypt(plain_text, key))


if __name__ == "__main__":
    main()
