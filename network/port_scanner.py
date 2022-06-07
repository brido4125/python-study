import ipaddress
import sys
import socket


# 열린 포트를 찾는 메서드 정의
def find_opened_port(ip_address):
    for port in range(0, 1024):#포트넘버 0~1024까지 iter
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPV4 + TCP 방식의 socket 객체 생성
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#socket close할 경우 바로 재사용 하도록 설정
        res = sock.connect_ex((ip_address, port))  # 인자로 받은 IP주소와 iter 중인 port로 커넥션 연결
        if res == 0:#결과가 0이면 open된 포트
            try:
                service = socket.getservbyport(port, 'tcp')#포트넘버로 해당 포트의 서비스명을 얻기 위해 사용,닫힌 경우를 위해 try-except 사용
                print(f'Port {port} ({service}) is Opened')
            except:
                pass
        sock.close()#연결 닫아주기


length = len(sys.argv)#들어온 인자의 갯수를 정수화

target_start_host = sys.argv[1]# 첫번째 인자 값을 변수화

if length == 2:#인자가 하나 들어올 경우 처리
    find_opened_port(target_start_host)

if length == 3:#인자가 둘 들어올 경우 처리
    target_end_host = sys.argv[2]#마지막 범위의 IP 주소 변수화
    int_ip1 = int(ipaddress.IPv4Address(target_start_host))#IP값 정수화
    int_ip2 = int(ipaddress.IPv4Address(target_end_host))#IP값 정수화
    for int_addr in range(int_ip1, int_ip2 + 1):#첫번째 인자의 IP ~ 두번째 인자의 IP까지 Iter하면서 모든 IP에 대해 포트 스캔 진행
        address = str(ipaddress.IPv4Address(int_addr)) #정수화된 IP를 다시 문자열 IP로 변환
        print("[address = ", address, "]") # 출력
        find_opened_port(address)# 포트 스캔하는 메서드 호출
