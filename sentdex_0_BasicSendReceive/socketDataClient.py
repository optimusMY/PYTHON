import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is IPV4 and SOCK_STREAM is TCP
s.connect((socket.gethostname(), 1234))  # gethostname() gets localhost ip, 1234 is port

full_msg = ""

while True:
    msg = s.recv(1024)  # receive buffer 1024 is chunk size  (chunk is how many bytes you wanna receive at once)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")


print(full_msg)


