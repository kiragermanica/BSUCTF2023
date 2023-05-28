enc_flag = "QbdRcUjXNS^]cNTeT]NZ]^fl"

for j in range(0, 255):
    flag = ""
    for i in enc_flag.encode():
        flag += chr((i - j) % 256)
    if 'bsuctf' in flag:
        print(flag)
        break
