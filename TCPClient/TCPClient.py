from socket import *

host= "10.20.1.54"
port = 9000

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host,port))
while True:
    data = input("message: ")
    sock.send(data.encode("utf-8")
    print("response: ", sock.recv(1024).decode("utf-8"))
