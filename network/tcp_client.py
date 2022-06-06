import socket

server_host = '127.0.0.1'
server_port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#포트번호 재사용

sock.connect((server_host,server_port))

msg = b'message'
#sock.sendto(msg,(server_host,server_port))
sock.sendall(msg)

sock.close()
