import heapq
import sys

N = int(input())
pq = []
for i in range(N):
    input_num = int(sys.stdin.readline())
    elem = (abs(input_num),input_num)
    if elem[0] == 0:#0이 들어온 경우
        if len(pq) != 0:
            heappop = heapq.heappop(pq)
            print(heappop[1])
        else:
            print(0)
    else:
        heapq.heappush(pq,elem)
