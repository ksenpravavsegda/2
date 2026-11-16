import socket

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("TCP-сервер запущено.")
print("Чекаємо на клієнта...")

conn, addr = server.accept()

with conn:
    print("Клієнт вже підключився:", addr)
    
    data = conn.recv(1024).decode("utf-8")
    print("Повідомлення від клієнта:", data)
    
    conn.sendall("Повідомлення отримано!".encode("utf-8"))

server.close()
print("Сервер завершив роботу.")

