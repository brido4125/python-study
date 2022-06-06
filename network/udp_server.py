#!usr/local/bin/python3

import socket

host = 'localhost'
port = 12345


#소켓 객체 생성
#1번째 인자 : Socket Family -> socket.AF_INET -> IPV4 사용함
#2번째 인자 : Socket Type -> SOCK_DGRAM(UDP) or SOCK_STREAM(TCP)
#3번째 인자 : socket.IPPROTO_UDP or TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#포트번호 재사용

#Binding
sock.bind((host,port))

# 소켓 서버 동작 구현
(data,address) = sock.recvfrom(65565)
print(len(data))
print(address)

# close
sock.close()

