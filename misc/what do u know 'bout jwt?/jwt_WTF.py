import jwt
import itertools

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImtpcmEiLCJhZG1pbiI6dHJ1ZX0.TqscY_8RBqxIw-Wg_KYs68J1lAuseB3uAIFLeOy4VM4'

import codecs


with codecs.open('/usr/share/wordlists/rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        secret = line.strip()
        try:
            decoded = jwt.decode(token, secret, algorithms=['HS256'])
            print(f"Secret found: {secret}")
            break
        except:
            pass
