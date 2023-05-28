from pwn import * # pip install pwntools
import json
import base64
from Crypto.Util.number import *
import codecs

r = remote('34.105.65.235', 31337)

def json_recv():
    line = r.recv()
    print(line.decode())
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



def from_base64(data):
    return base64.b64decode(data).decode()

def from_base32(data):
    return base64.b32decode(data).decode()

def from_base16(data):
    return base64.b16decode(data).decode()

def from_hex(data):
    return bytes.fromhex(data).decode('utf-8')

def from_rot13(data):
    return codecs.decode(data, 'rot-13')

to_send = {
    "decoded": "changeme"
}



if __name__ == "__main__":
    for i in range(100):
        data = json_recv()
        print(data)
        answer={} 
        if data["type"] == "base_64":
            answer={"decoded":from_base64(data["encoded"])}
        elif data["type"] == "hex":
            answer={"decoded":from_hex(data["encoded"])}
        elif data["type"] == "base_32":
            answer={"decoded":from_base32(data["encoded"])}
        elif data["type"] == "rot13":
            answer={"decoded":from_rot13(data["encoded"])}
        elif data["type"] == "base_16":
            answer={"decoded":from_base16(data["encoded"])}
        print("[+] Answer = ", answer)
        json_send(answer)
        print(r.recv().decode())

    print(r.recv().decode())


