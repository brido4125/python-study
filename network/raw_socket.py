import socket

# Permission Error => Sudo 권한 필요
import struct

upper_raw_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)  # 3번째 인자 생략 불가 (TCP or UDP) -> Layer 4
upper_raw_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)# 직접 IP 헤더를 생성한다 -> Layer 3까지 다뤄야함

lower_raw_sock = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))

source_port = 4321
dest_port = 22

length = 0
checksum = 0

# '!HHHH' => UDP 포맷 스트링
upd_header = struct.pack('!HHHH', source_port, dest_port, length, checksum)

#s.sendto vs send 차이점

# Ethernet => IP => TCP => HTTP

#arp_spoofing,LAND 공격,DDOS(DOS 공격을 여러개)-fluooding
