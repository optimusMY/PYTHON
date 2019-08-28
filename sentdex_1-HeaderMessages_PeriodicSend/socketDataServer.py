import socket
import time

HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is IPV4 and SOCK_STREAM is TCP
s.bind((socket.gethostname(), 1235))  # gethostname() gets localhost ip, 1234 is port
s.listen(5)  # s behaves like server

msgcnt = 0

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    msgcnt += 1
    msg = "welcome to the server!--" + str(msgcnt)
    msg = f'{len(msg):<{HEADERSIZE}}' + msg  #adding a fixed length Header by padding the message

    clientsocket.send(bytes(msg, "utf-8"))

    # send periodic messages (sending timestamp)
    while True:
        time.sleep(3)
        msg = f"The time is: {time.localtime()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg  #wrapping with header
        clientsocket.send(bytes(msg, "utf-8"))








