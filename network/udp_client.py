#!usr/local/bin/python3.9
import socket

server_host = '127.0.0.1'
server_port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#포트번호 재사용

print(sock)
msg = b'message'
sock.sendto(msg,(server_host,server_port))
sock.close()


