#!/usr/bin/env python3

#University of Victoria (UVIC)
#SENG360 Lab 1 exercise
#Charles Yang


import sys
from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify

def main():
    file = sys.stdin
    plaintext = 'This is a top secret.'
    iv = unhexlify('aabbccddeeff00998877665544332211')
    ciphertext = unhexlify('764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2')

    for line in file:
        key = line.rstrip("\n")
        pad = 32 - len(plaintext)
        if len(key) < 16:
            okey = key
            key = key + ('#'*(16-(len(key))))
        if len(key) > 16:
            continue
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypt = cipher.decrypt(ciphertext)
        decrypt = decrypt[:-pad]
        #decrypt = decrypt.decode()
        if decrypt == plaintext:
            print('The key is: {}'.format(okey))
            sys.exit()


if __name__ == "__main__":
    main()
