#!/usr/bin/python3

import random

if __name__ == "__main__":
    flag = "redacted_flag"
    enc_flag = ""
    key = random.randint(0, 255)
    for i in flag.encode():
        enc_flag += chr((i + key) % 256)
    print(enc_flag) # QbdRcUjXNS^]cNTeT]NZ]^fl 
