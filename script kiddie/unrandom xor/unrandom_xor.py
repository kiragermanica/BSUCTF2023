import random

with open("data.enc", "rb") as f:
    enc = f.readline()
    for i in range(0, 100000):
        random.seed(i)
        rand = random.randbytes(len(enc))
        FLAG = bytes(i ^ j for i, j in zip(enc, rand))
        if b'bsuctf' in FLAG:
            print(FLAG.decode())
            break
