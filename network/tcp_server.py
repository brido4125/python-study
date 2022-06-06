import socket

host = 'localhost'
port = 12345

parent = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
parent.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
parent.bind((host,port))

parent.listen(10)#10대의 client가 접속가능

(child,address) = parent.accept()

#(data,address) = child.recvfrom(65565)
data = child.recv(65565)#TCP는 이거 사용

print(len(data))
print(data)

child.close()
parent.close()
