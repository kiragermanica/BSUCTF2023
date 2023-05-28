import random

random.seed(?????) # len(seed) = 5

FLAG = b"bsuctf{redacted_flag}"

random = random.randbytes(len(FLAG))

enc = bytes(i ^ j for i, j in zip(FLAG, random))

with open("data.enc", "wb") as f:
    f.write(enc)
