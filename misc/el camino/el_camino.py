import pyAesCrypt

input_file = "encrypted.aes"
output_file = "jesse.png"

password = "jessepinkman"
buffer_size = 256 * 1024

with open(input_file, "rb") as input_f, open(output_file, "wb") as output_f:
    input_length = len(input_f.read())
    input_f.seek(0)
    pyAesCrypt.decryptStream(input_f, output_f, password, buffer_size, input_length)

