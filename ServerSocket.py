import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind((socket.gethostname(), 9500))
serv.listen(5)


while True:
    conn, addr = serv.accept()
    msg = conn.recv(1024)
    print(msg.decode("utf-8"))
    conn.send(bytes("Hi", "utf-8"))