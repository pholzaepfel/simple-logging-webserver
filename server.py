#!/usr/bin/python
#python2 because lazy
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8099
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

def handle_client(client_socket):
    request = client_socket.recv(4096)
    print (request)
    out = open("log.txt","a")
    out.writelines(request)
    out.close()

    client_socket.send("HTTP 1/1 200 OK\r\n")
    client_socket.close()

while True:
        client,addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
