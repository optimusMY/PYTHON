import socket
import time
import pickle




HEADERSIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is IPV4 and SOCK_STREAM is TCP
s.bind((socket.gethostname(), 1236))  # gethostname() gets localhost ip, 1234 is port
s.listen(5)  # s behaves like server



while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")

    dicty = {1: "Hey", 2: "There"}
    msg = pickle.dumps(dicty)
    #print(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg  #adding a fixed length Header by padding the message

    clientsocket.send(msg)
