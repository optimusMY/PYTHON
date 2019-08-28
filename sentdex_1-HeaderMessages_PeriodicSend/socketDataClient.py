import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is IPV4 and SOCK_STREAM is TCP
s.connect((socket.gethostname(), 1235))  # gethostname() gets localhost ip, 1234 is port



while True:
    full_msg = ""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message len: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False  # clear flag to finish new messag reception because we complete matching length message as to header

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("whole message received!")
            print((full_msg[HEADERSIZE:]))    #(print the message except header part) print subsequent data after HEADERSIZE bytes in the full_msg
            new_msg = True  # means accept new messages as long as message reception is not complete
            full_msg = ""

print(full_msg)


