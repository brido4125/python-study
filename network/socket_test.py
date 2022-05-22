import socket
import struct

getservbyname = socket.getservbyname('ssh', 'tcp')

print(getservbyname)

print(socket.gethostname())

print(socket.gethostbyname('naver.com'))
print(socket.gethostbyname('hongchangsub.com'))

# network == big endian -> 해결해주는것이 struct module

#1이라는 숫자를 빅 엔디안으로 만들어줘 h -> short type
print(struct.pack('>h',1)) # big endian
print(struct.pack('<h',1)) # little endian

print(struct.pack('>2h',1,2))
print(struct.pack('<2h',1,2))

pack = struct.pack('!2h2q', 1, 2, 3, 4)
print(struct.unpack('!2h2q',pack))

aton = socket.inet_aton('127.0.0.1') # ASCII to Network(Big endian)
unpack = struct.unpack('!i', aton) # tuple에 정수
socket.inet_ntoa(struct.pack('!i',unpack[0])) # Network to ASCII

stoi