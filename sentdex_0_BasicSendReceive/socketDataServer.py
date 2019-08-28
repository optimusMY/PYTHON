import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is IPV4 and SOCK_STREAM is TCP
s.bind((socket.gethostname(), 1234))  # gethostname() gets localhost ip, 1234 is port
s.listen()  # s behaves like server

while True:
    clientsocket, address = s.accept()
    print("connection from {address} has been established!")
    clientsocket.send(bytes("welcome to the server!", "utf-8"))
    clientsocket.close()






