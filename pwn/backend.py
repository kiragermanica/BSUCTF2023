import socket
import threading
import codecs
import json
import random
import base64
import binascii


def base_64(x):
    return base64.b64encode(x).decode('utf-8')

def base_32(x):
    return base64.b32encode(x).decode('utf-8')

def base_16(x):
    return base64.b16encode(x).decode('utf-8')

def rot13(x):
    return codecs.encode(x.decode(), 'rot_13')

def hex(x):
    return binascii.hexlify(x).decode('utf-8')

ALGORITHMS = [base_64, base_32, base_16, rot13, hex]

# Задайте сообщения для шифрования и количество заданий
MESSAGES = [b"Hello, nigger!", b"Python is awesome!", b"Security is important!", b"Cryptography is important!", b"Try again!"]
NUM_QUESTIONS = 33


def generate_question():
    # Выбираем случайное сообщение и алгоритм шифрования
    message = random.choice(MESSAGES)
    algorithm = random.choice(ALGORITHMS)
    if random.randrange(1,500) == 333:
        message = b"bsuctf{s0m3t1m35_y0u_sh0u1d_st4y_4nd_w4tch}"
    # Шифруем сообщение с использованием алгоритма
    encrypted_message = algorithm(message)

    # Формируем JSON-объект с зашифрованным сообщением
    data = {"type":algorithm.__name__,"encoded": encrypted_message}

    return data, message, algorithm, algorithm.__name__


# Функция для обработки клиентских запросов
def handle_client(client_socket):
    try:
        correct_answers = 0

        # Обрабатываем 100 клиентских запросов
        for i in range(NUM_QUESTIONS):
            # Генерируем вопрос
            question, answer, algorithm, algorithm_name = generate_question()
            if b"bsuctf" in answer:
                answer=answer.decode()
                client_socket.sendall(b"<============================ Golden Connection ============================>\n")
                client_socket.sendall(b"<============================  Congratulations  ============================>\n")
                client_socket.sendall(b"<=========================  Your side-quest Flag  ==========================>\n")
                client_socket.sendall(f"<================ {answer} ==============>\n".encode())
                break
            # Отправляем клиенту вопрос в формате JSON
            client_socket.sendall((str(question).replace("'",'"')+"\n").encode())

            # Получаем ответ от клиента в формате JSON
            try:
                response = json.loads(client_socket.recv(1024).decode())
                # Расшифровываем ответ клиента с использованием выбранного алгоритма
                decrypted_response = response["decoded"]

                # Проверяем, правильно ли расшифрован ответ клиента
                if decrypted_response == answer.decode():
                    correct_answers += 1
                    client_socket.sendall("[+] Correct!\n".encode())
                else:
                    client_socket.sendall("[!] Incorrect. Bye!".encode())
                    client_socket.close()
                    break

                if correct_answers == NUM_QUESTIONS:
                    client_socket.sendall(b"bsuctf{kn0ck_kn0ck_s0ck3t5_kn0ck_kn0ckkk}")
            except json.JSONDecodeError:
                client_socket.sendall("[!] Data should be in JSON format!".encode())
                client_socket.close()
                break

        client_socket.close()
    except socket.timeout:
        client_socket.sendall("[!] Not fast enough =(\n".encode())
        client_socket.close()




def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_port = 31337
    server_socket.bind(('0.0.0.0', server_port))
    server_socket.listen()
    print(f"Server listening on port {server_port}...")
    while True:
        client_socket, client_address = server_socket.accept()
        client_socket.settimeout(2) 
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    try:
        run_server()  
    except KeyboardInterrupt:
        quit()
