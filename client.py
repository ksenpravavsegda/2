import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = input("Введіть повідомлення яке очете відправити серверу: ")
client.sendall(message.encode("utf-8"))

response = client.recv(1024).decode("utf-8")
print("Відповідь сервера:", response)

client.close()