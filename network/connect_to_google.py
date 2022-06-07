import socket

s_host= 'www.google.com'
s_port = 80

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((s_host,s_port))#DNS 써도 되고 그냥 IP주소 써도 됨

print(sock)
print(f'Socket is connected to {s_host}')

msg = b'GET / HTTP/1.1\r\n\r\n'
sock.sendall(msg)

data = sock.recv(65565)

print(data)

sock.close()